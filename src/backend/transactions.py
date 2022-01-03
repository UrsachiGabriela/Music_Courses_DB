from src.backend.connection import DBConnection


class Transaction:

    # functie pt completarea unei fise de inscriere
    # daca nu mai sunt locuri la curs sau daca acel curs este programat in timpul altui curs la care este inscris cursantul si inca
    # nu l-a finalizat , inscrierea nu se realizeaza (prin evitarea suprapunerii programului este inclus si cazul in care
    # un cursant doreste sa se inscrie la un curs la care este deja inscris )

    @staticmethod
    def add_registration_form(dbconnection:DBConnection,i_cursant:int,i_curs:int):


        register_cmd=f"""
        DECLARE
            nInscrisi NUMBER;
            nMax NUMBER;

            
            oraCurs DATE;
            ziCurs VARCHAR2(20) ; 
            suprapunereProgram NUMBER;
            
        BEGIN    
            SAVEPOINT inscrieCursant;
                    INSERT INTO fisa_inscriere(data_inscriere,id_cursant,id_curs) VALUES (to_date(sysdate ,'dd-mon-yyyy'),:i_cursant1 ,:i_curs1);
                    UPDATE cursuri SET nr_inscrisi=nr_inscrisi+1 WHERE id_curs=:i_curs2 ;
                    
                    
                    
                    
                    
                    SELECT nr_inscrisi INTO nInscrisi FROM cursuri WHERE id_curs=:i_curs3 ;
                    SELECT max_locuri INTO nMax FROM cursuri WHERE id_curs=:i_curs4;
                    
                   
                    
                    
                    
                                        
                    SELECT ora
                    INTO oraCurs
                    FROM program
                    WHERE id_curs=:i_curs5;
                    
                    SELECT zi
                    INTO ziCurs
                    FROM program
                    WHERE id_curs=:i_curs6;
        
                    
                    with 
                    programElev as 
                    (
                        SELECT cursanti.id_cursant, nume, cursuri.id_curs,zi,to_char(ora,'hh24:mi') AS ora,sala
                        FROM cursanti , cursuri, program,fisa_inscriere
                        WHERE cursuri.id_curs=program.id_curs
                            AND cursuri.id_curs=fisa_inscriere.id_curs
                            AND cursanti.id_cursant=fisa_inscriere.id_cursant
                            AND cursanti.id_cursant = :i_cursant2
                            AND nota_evaluare is null  
                    )
                    
                   
        
                    SELECT COUNT(*)
                    INTO suprapunereProgram
                    FROM programElev
                    WHERE zi = ziCurs 
                        AND 2 > abs(to_number((oraCurs-to_date(ora,'HH24:MI'))*24));
        
                            
                    
                    
                    
                    
                    
                    
                    IF nInscrisi>nMax OR suprapunereProgram>1 THEN
                        ROLLBACK TO inscrieCursant;
                    ELSE
                        COMMIT;
                    END IF;           
        END;
        """

        #verific daca s-a realizat inscrierea sau a fost executata ramura cu rollback
        verify_cmd=f"""
        SELECT COUNT(*)  from fisa_inscriere
        WHERE id_cursant=:i_cursant and id_curs=:i_curs
        """

        #interogare inainte de a efectua tranzactia
        response1=dbconnection.fetch_data(verify_cmd,[i_cursant,i_curs])
        r1=[row for row in response1]
        if r1:
            count1=int(r1[0][0])
        else:
            count1=0

        #efectuarea tranzactiei
        exec=dbconnection.exec_cmd(register_cmd,[i_cursant,i_curs,i_curs,i_curs,i_curs,i_curs,i_curs,i_cursant])

        #interogare dupa efectuarea tranzactiei
        response2=dbconnection.fetch_data(verify_cmd,[i_cursant,i_curs])
        r2=[row for row in response2]
        if r2:
            count2=int(r2[0][0])
        else:
            count2=0


        if exec and count1==0 and count2==1:
            return True # inscrierea s-a realizat cu succes (inainte de tranzactie cursantul nu era inscris - count1=0- ;
                        #                                    dupa tranzactie fisa de inscriere este inregistrata in baza de date -count2=1- )
        else:
            #print('nu s-a realizat inscrierea : fie nu mai sunt locuri la cursul solicitat, fie cursantul e deja ocupat')
            return False # nu s-a realizat inscrierea



    # functie apelata la finalizarea unui curs de catre un cursant (solicitare explicita)
    # voi avea posibilitatea sa apelez aceasta functie doar daca nota evaluare is null (daca nu e deja finalizat cursul )
    @staticmethod
    def unregister_from_course(dbconnection:DBConnection,id_cursant:int,id_curs:int,nota_evaluare:int):
        end_cmd=f"""
        BEGIN
            UPDATE fisa_inscriere SET nota_evaluare=:nota WHERE id_cursant=:id_cursant1 AND id_curs=:id_curs1;
            UPDATE cursuri SET nr_inscrisi = nr_inscrisi-1 WHERE id_curs=:id_curs2;
        END;
        """

        exec=dbconnection.exec_cmd(end_cmd,[nota_evaluare,id_cursant,id_curs,id_curs])
        if exec:
            return True
        else:
            return False


    # functie apelata periodic pentru a modifica baza de date la finalizarea cursurilor -> pot crea un thread separat pt aceasta functie
    # nota_evaluare va fi generata aleatoriu ( nu se ocupa secretariatul de stabilirea notei )
    @staticmethod
    def end_course(dbconnection:DBConnection,nota_evaluare:int):
        end_cmd=f"""
        BEGIN
            
            
            update cursuri c
            set nr_inscrisi = nr_inscrisi - (with temp 
                                                as (select id_curs,count(*)as nractualizari from fisa_inscriere
                                                    where data_inscriere in (select f.data_inscriere from fisa_inscriere f,cursuri c where f.id_curs=c.id_curs and c.durata * 30 + to_date(f.data_inscriere,'dd-mon-yy') <= to_date(sysdate,'dd-mon-yy') and nota_evaluare is  null)
                                                    group by id_curs)
                                                
                                                select nractualizari from temp where temp.id_curs=c.id_curs )   
            where exists   (with temp 
                                as (select id_curs,count(*)as nractualizari from fisa_inscriere
                                    where data_inscriere in (select f.data_inscriere from fisa_inscriere f,cursuri c where f.id_curs=c.id_curs and c.durata * 30 + to_date(f.data_inscriere,'dd-mon-yy') <= to_date(sysdate,'dd-mon-yy') and nota_evaluare is  null)
                                    group by id_curs)
                                                
                                select nractualizari from temp where temp.id_curs=c.id_curs) ;  
                                
                                
            update fisa_inscriere 
            set nota_evaluare = :nota
            where data_inscriere in (select f.data_inscriere from fisa_inscriere f,cursuri c where f.id_curs=c.id_curs and c.durata * 30 + to_date(f.data_inscriere,'dd-mon-yy') <= to_date(sysdate,'dd-mon-yy') and nota_evaluare is  null);

                                            
            
        END;
        """


        exec=dbconnection.exec_cmd(end_cmd,[nota_evaluare])
        if(exec):
            return True
        else:
            return False


    # functie pt adaugarea unui program de desfasurare pt un curs dat
    # evitarea suprapunerii programului pentru 2 cursuri diferite in aceeasi sala sau
    # suprapunerii programului unui profesor ce preda la mai multe cursuri
    @staticmethod
    def add_program(dbconnection:DBConnection,id_curs:int,zi:str,ora:str,sala:int):
        add_prog_cmd=f"""
        DECLARE 
            idp NUMBER ; 
            profCount NUMBER;
            roomCount NUMBER;
            
            BEGIN
                SAVEPOINT AddProgramCurs;
                    INSERT INTO program VALUES (:zi1,to_date(:ora1,'HH24:MI'),:sala1,:id_curs1);
            
            
            
                    WITH programProf AS  
                        (
                            SELECT p.id_profesor, prog.zi,to_char(prog.ora,'hh24:mi') AS "ORA" 
                            FROM profesori p,cursuri c,program prog
                            WHERE c.id_profesor=p.id_profesor
                                AND c.id_curs=prog.id_curs
                        )
                    
                    SELECT id_profesor 
                    INTO idp
                    FROM profesori,cursuri
                    WHERE profesori.id_profesor=cursuri.id_profesor
                    AND cursuri.id_curs=:id_curs2;
                    
                    SELECT COUNT(*) 
                    INTO profCount
                    FROM programProf
                    WHERE id_profesor = idp AND zi=:zi3 
                        AND 2 > abs(to_number((to_date(:ora3,'HH24:MI')-to_date(ora,'HH24:MI'))*24));
                        
            
            
            
                    WITH programSala  AS
                    (
                            SELECT  prog.zi,to_char(prog.ora,'hh24:mi') AS "ORA" ,prog.sala
                            FROM cursuri c,program prog
                            WHERE c.id_curs=prog.id_curs        
                    
                    )
                    

                    SELECT COUNT(*) 
                    INTO roomCount
                    FROM programSala
                    WHERE sala=:sala4 AND zi=:zi4 
                        AND 2 > abs(to_number((to_date(:ora4,'HH24:MI')-to_date(ora,'HH24:MI'))*24));
                        
                 
                    --daca profesorul e ocupat in intervalul respectiv sau este deja un curs in sala respectiva
                    IF profCount > 1 OR roomCount > 1 THEN
                        ROLLBACK TO AddProgramCurs;
                    ELSE 
                        COMMIT ;
                    END IF; 
                
                
            END;
        """


        exec=dbconnection.exec_cmd(add_prog_cmd,[zi,ora,sala,id_curs,id_curs,zi,ora,sala,zi,ora])

        verify_cmd=f"""
        SELECT COUNT(*)  from program
        WHERE zi=:v1 and ora=to_date(:v2,'HH24:MI') and sala=:v3
        """

        response=dbconnection.fetch_data(verify_cmd,[zi,ora,sala])
        r=[row for row in response]
        if r:
            count=int(r[0][0])
        else:
            count=0

        if exec and count==1:
            return True #programul a fost adaugat cu succes
        else:
            return False #programul nu poate fi adaugat



    @staticmethod
    def modify_course_duration(dbConnection:DBConnection,id_curs:int,durata:int):
        cmd=f"""
        DECLARE 
        n_i NUMBER; --nr inscrisi
        BEGIN
        
            SAVEPOINT modificareDurata;
            
                SELECT nr_inscrisi
                INTO n_i
                FROM cursuri
                WHERE id_curs=:id1;
                
                
                UPDATE cursuri
                SET durata=:d1
                WHERE id_curs=:i2;
                
                IF n_i != 0 THEN
                    ROLLBACK to modificareDurata;
                ELSE
                    COMMIT;
                END IF;
                
                
        END;
        """


        verify_cmd=f"""
        SELECT nr_inscrisi FROM cursuri WHERE id_curs=:id
        """

        response=dbConnection.fetch_data(verify_cmd,[id_curs])
        r=[row for row in response]
        if r:
            nr=int(r[0][0])
        else:
            nr=-1

        if nr==0:
            if dbConnection.exec_cmd(cmd,[id_curs,durata,id_curs]):
                return True
            else:
                return False
        else:
            return False




    @staticmethod
    def modify_course_reg_fee(dbConnection:DBConnection,id_curs:int,taxa:int):
        cmd=f"""
        DECLARE 
        n_i NUMBER; --nr inscrisi
        BEGIN
        
            SAVEPOINT modificareTaxa;
            
                SELECT nr_inscrisi
                INTO n_i
                FROM cursuri
                WHERE id_curs=:id1;
                
                
                UPDATE cursuri
                SET taxa_inscriere=:t1
                WHERE id_curs=:i2;
                
                IF n_i != 0 THEN
                    ROLLBACK to modificareTaxa;
                ELSE
                    COMMIT;
                END IF;
                
                
        END;
        """


        verify_cmd=f"""
        SELECT nr_inscrisi FROM cursuri WHERE id_curs=:id
        """

        response=dbConnection.fetch_data(verify_cmd,[id_curs])
        r=[row for row in response]
        if r:
            nr=int(r[0][0])
        else:
            nr=-1

        if nr==0:
            if dbConnection.exec_cmd(cmd,[id_curs,taxa,id_curs]):
                return True
            else:
                return False
        else:
            return False





    @staticmethod
    def modify_mail(dbConnection:DBConnection,id_cursant:int,mail:str):
        cmd=f"""
        UPDATE detalii_cursanti
        SET email=:m
        WHERE id_cursant = :id 
        """

        if dbConnection.exec_cmd(cmd,[mail,id_cursant]):
            return True
        else:
            return False


    @staticmethod
    def modify_prof(dbConnection:DBConnection,id_prof:int,name:str):
        cmd=f"""
        UPDATE profesori
        SET nume=:n
        WHERE id_profesor=:id
        """

        if dbConnection.exec_cmd(cmd,[name,id_prof]):
            return True
        else:
            return False

    # sql_command = f"""
    #     BEGIN
    #         delete from  profesori where id_profesor=1022;
    #         delete from  profesori where id_profesor=2423;
    #     END;
    #     """
from src.backend.connection import DBConnection


class Transaction:

    # functie pt completarea unei fise de inscriere
    # daca nu mai sunt locuri la curs sau daca acel curs este programat in timpul altui curs la care este inscris cursantul si inca
    # nu l-a finalizat , inscrierea nu se realizeaza
    @staticmethod
    def registerToCourse(dbconnection:DBConnection,d_inscriere:str,i_cursant:int,i_curs:int):
        #prin variabila nrInscrieri rezolv situatia in care un cursant incearca sa se inscrie la un curs la care era deja inscris
        # pot face asta si atunci cand incerc inscrierea -> cu o interogare, vad daca e necesar sa mai apelez tranzactia sau nu!!!
        # TO DO : a doua varianta!!!!!

        register_cmd=f"""
        DECLARE
            nInscrisi NUMBER;
            nMax NUMBER;

            
            oraCurs DATE;
            ziCurs VARCHAR2(20) ; 
            suprapunereProgram NUMBER;
            
        BEGIN    
            SAVEPOINT inscrieCursant;
                    INSERT INTO fisa_inscriere(data_inscriere,id_cursant,id_curs) VALUES (to_date(:d_inscriere ,'dd-mon-yyyy'),:i_cursant1 ,:i_curs1);
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

        exec=dbconnection.exec_cmd(register_cmd,[d_inscriere,i_cursant,i_curs,i_curs,i_curs,i_curs,i_curs,i_curs,i_cursant])

        response=dbconnection.fetch_data(verify_cmd,[i_cursant,i_curs])
        r=[row for row in response]
        count=int(r[0][0])


        if exec and count==1:
            return True # inscrierea s-a realizat cu succes
        else:
            print('nu s-a realizat inscrierea : fie nu mai sunt locuri la cursul solicitat, fie cursantul e deja ocupat')
            return False # nu s-a realizat inscrierea


        # acolo unde apelez aceasta functie :
        #  - verific daca am in tabela fisa_inscriere tupla (id_curs,id_cursant) pe care vreau sa o introduc
        #   -in caz afirmativ, nu mai apelez la aceasta tranzactie si afisez un mesaj de tipul "e deja inscris"
        #   - in caz negativ, apelez la tranzactie ; pt a verifica daca s-a dat commit sau nu, folosesc verify_cmd care imi
        #                                            spune  daca am introdus ce am vrut in tabela sau nu

    # functie apelata la finalizarea unui curs de catre un cursant
    @staticmethod
    def endCourse(dbconnection:DBConnection,id_cursant:int,id_curs:int,nota_evaluare:int):
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


    # functie pt adaugarea unui program de desfasurare pt un curs dat
    @staticmethod
    def addProgram(dbconnection:DBConnection,id_curs:int,zi:str,ora:str,sala:int):
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
        if exec:
            return True
        else:
            return False




    # sql_command = f"""
    #     BEGIN
    #         delete from  profesori where id_profesor=1022;
    #         delete from  profesori where id_profesor=2423;
    #     END;
    #     """
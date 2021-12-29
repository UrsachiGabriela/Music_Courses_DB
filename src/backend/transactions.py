from src.backend.connection import DBConnection


class Transaction:


    @staticmethod
    def registerToCourse(dbconnection:DBConnection,data_inscriere:str,id_cursant:int,id_curs:int):
        #prin variabila nrInscrieri rezolv situatia in care un cursant incearca sa se inscrie la un curs la care era deja inscris
        # pot face asta si atunci cand incerc inscrierea -> cu o interogare, vad daca e necesar sa mai apelez tranzactia sau nu!!!
        # TO DO : a doua varianta!!!!!

        register_cmd=f"""
        DECLARE
            nInscrisi NUMBER;
            nMax NUMBER;
            nrInscrieri NUMBER;
            
        BEGIN    
            SAVEPOINT inscrieCursant;
                    INSERT INTO fisa_inscriere(data_inscriere,id_cursant,id_curs) VALUES (to_date({data_inscriere},'dd-mon-yyyy'),{id_cursant},{id_curs});
                    UPDATE cursuri SET nr_inscrisi=nr_inscrisi+1 WHERE id_curs={id_curs} ;
                    
                    SELECT nr_inscrisi INTO nInscrisi FROM cursuri WHERE id_curs={id_curs} ;
                    SELECT max_locuri INTO nMax FROM cursuri WHERE id_curs={id_curs};
                    
                    SELECT COUNT(*) INTO nrInscrieri from fisa_inscriere WHERE id_cursant={id_cursant} and id_curs={id_curs}
                    
                    
                    IF nInscrisi>nMax OR nrInscrieri > 1 THEN
                        ROLLBACK TO inscrieCursant;
                    ELSE
                        COMMIT;
                    END IF;           
        END;
        /
        """

        #verific daca s-a realizat inscrierea sau a fost executata ramura cu rollback
        verify_cmd=f"""
        BEGIN
            SELECT COUNT(*)  from fisa_inscriere
            WHERE id_cursant={id_cursant} and id_curs={id_curs}
        END;
        """

        response=dbconnection.fetch_data(verify_cmd)
        r=[row for row in response]
        count=int(r[0][0])


        if dbconnection.exec_cmd(register_cmd) and count==1:
            return True
        else:
            return False


        # acolo unde apelez aceasta functie :
        #  - verific daca am in tabela fisa_inscriere tupla (id_curs,id_cursant) pe care vreau sa o introduc
        #   -in caz afirmativ, nu mai apelez la aceasta tranzactie si afisez un mesaj de tipul "e deja inscris"
        #   - in caz negativ, apelez la tranzactie ; pt a verifica daca s-a dat commit sau nu, folosesc verify_cmd care imi
        #                                            spune  daca am introdus ce am vrut in tabela sau nu

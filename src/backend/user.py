from src.backend.connection import DBConnection


class User:
    @staticmethod
    def registerLearner(dbconnection:DBConnection,nume:str,varsta:int,ocupatie:str,gen:str,email:str):
        add_learner_cmd = f"""
        BEGIN
            INSERT INTO cursanti(nume,varsta,ocupatie) VALUES (:nume1,:varsta1,:ocupatie1);
            INSERT INTO detalii_cursanti VALUES (:gen1,:email1,cursanti_id_cursant_seq.CURRVAL);
        END;
        """

        exec=dbconnection.exec_cmd(add_learner_cmd,[nume,varsta,ocupatie,gen,email])
        if exec:
            return True
        else:
            return False
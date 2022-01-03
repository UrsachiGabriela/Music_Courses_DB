from src.backend.connection import DBConnection
from src.backend.transactions import Transaction


class User:

    #functie pentru introducerea unui cursant in baza de date
    @staticmethod
    def introduce_learner(dbconnection:DBConnection,nume:str,varsta:int,ocupatie:str,gen:str,email:str):
        add_learner_cmd = f"""
        BEGIN
            INSERT INTO cursanti(nume,varsta,ocupatie) VALUES (:nume1,:varsta1,:ocupatie1);
            INSERT INTO detalii_cursanti VALUES (:gen1,:email1,cursanti_id_cursant_seq.CURRVAL);
        END;
        """

        exec=dbconnection.exec_cmd(add_learner_cmd,[nume,varsta,ocupatie,gen,email])
        if exec:
            return True #am introdus cursantul in baza de date
        else:
            return False #cursantul este deja in baza de date sau au fost introduse gresit datele


    #id_cursant si id_curs, fiind FK, vor fi selectate din interfata
    @staticmethod
    def register_learner_to_course(dbconnection:DBConnection,id_cursant:int,id_curs:int):
        if Transaction.add_registration_form(dbconnection,id_cursant,id_curs):
            return True
        else:
            return False

    @staticmethod
    def unregister_learner_from_course(dbconnection:DBConnection,id_cursant:int,id_curs:int,nota_evaluare:int):
        if Transaction.unregister_from_course(dbconnection,id_cursant,id_curs,nota_evaluare):
            return True
        else:
            return False




    @staticmethod
    def add_course(dbconnection:DBConnection,durata:int,max_locuri:int,nr_inscrisi:int,instrument:str,taxa:int,id_prof:int):
        add_course_cmd=f"""
            INSERT INTO cursuri(id_profesor,durata,max_locuri,nr_inscrisi,instrument,taxa_inscriere) VALUES (:id_p,:d,:max_l,:nr_ins,:instr,:taxa)
        """

        exec=dbconnection.exec_cmd(add_course_cmd,[id_prof,durata,max_locuri,nr_inscrisi,instrument,taxa])
        if exec:
            return True
        else:
            return False

    @staticmethod
    def add_prof(dbconnection:DBConnection,nume:str):
        add_prof_cmd=f"""
            INSERT INTO profesori(nume) VALUES (:n)
        """

        exec=dbconnection.exec_cmd(add_prof_cmd,[nume])
        if exec:
            return True
        else:
            return False

    @staticmethod
    def add_prog(dbconnection:DBConnection,id_curs:int,zi:str,ora:str,sala:int):
        if Transaction.add_program(dbconnection,id_curs,zi,ora,sala):
            return True
        else:
            return False








    @staticmethod
    def get_prof_prog(dbConnection:DBConnection):
        cmd=f"""
            SELECT profesori.id_profesor,nume,zi,to_char(ora,'hh24:mi') AS ora,sala
            FROM profesori,cursuri,program
            WHERE profesori.id_profesor=cursuri.id_profesor
                AND cursuri.id_curs=program.id_curs
        """

        response=dbConnection.fetch_data(cmd,[])
        return response

    @staticmethod
    def update_mail(dbConnection:DBConnection,id_cursant:int,mail:str):
        if Transaction.modify_mail(dbConnection,id_cursant,mail):
            return True
        else:
            return False

    @staticmethod
    def modify_course_duration(dbConnection:DBConnection,id_curs:int,durata:int):
        return Transaction.modify_course_duration(dbConnection,id_curs,durata)

    @staticmethod
    def modify_course_reg_fee(dbConnection:DBConnection,id_curs:int,taxa:int):
        return Transaction.modify_course_reg_fee(dbConnection,id_curs,taxa)

    @staticmethod
    def modify_prof(dbConnection:DBConnection,id_prof:int,name:str):
        return Transaction.modify_prof(dbConnection,id_prof,name)

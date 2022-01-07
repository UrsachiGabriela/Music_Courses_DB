import tkinter as tk

from src.backend.connection import DBConnection
from src.backend.user import User
from src.frontend.pages.BasePage import BasePage
from src.frontend.pages.CoursesPage import CoursesPage
from src.frontend.pages.LearnersPage import LearnersPage
from src.frontend.pages.ProfessorsPage import ProfessorsPage


class App(tk.Tk):
    def __init__(self,db_connection: DBConnection):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self,"Music School")

        self.db_connection = db_connection

        self.container=tk.Frame(self,bg='gray97')
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)


        self.frames={}
        for F in (LearnersPage,CoursesPage,BasePage,ProfessorsPage):
            page_name=F.__name__
            frame=F(parent=self.container,controller=self)
            self.frames[page_name]=frame
            frame.grid(row=0, column=0, sticky="nesw")
        self.show_frame('BasePage')





    def show_frame(self , name):
        frame=self.frames[name]
        frame.init()
        frame.tkraise()

    def get_columns_name(self, table_name):
        query = f"""SELECT column_name FROM USER_TAB_COLUMNS WHERE lower(table_name) =:tb"""
        response=self.db_connection.fetch_data(query,[table_name])
        query_results = [row for row in response]
        return query_results

    def add_learner(self,nume:str,varsta:int,ocupatie:str,gen:str,email:str):
        return User.introduce_learner(self.db_connection,nume,varsta,ocupatie,gen,email)

    def register_to_course(self,id_cursant:int,id_curs:int):
        return User.register_learner_to_course(self.db_connection,id_cursant,id_curs)

    def unregister_from_course(self,id_cursant:int,id_curs:int,nota_evaluare=3):
        return User.unregister_learner_from_course(self.db_connection,id_cursant,id_curs,nota_evaluare)

    def update_mail(self,id_cursant:int,mail:str):
        return User.update_mail(self.db_connection,id_cursant,mail)


    def add_course(self,durata:int,max_locuri:int,nr_inscrisi:int,instrument:str,taxa:int,id_prof:int):
        return User.add_course(self.db_connection,durata,max_locuri,nr_inscrisi,instrument,taxa,id_prof)

    def add_program(self,id_curs:int,zi:str,ora:str,sala:int):
        return User.add_prog(self.db_connection,id_curs,zi,ora,sala)

    def update_course_duration(self,id_curs:int,durata:int):
        return User.modify_course_duration(self.db_connection,id_curs,durata)

    def update_course_reg_fee(self,id_curs:int,taxa:int):
        return User.modify_course_reg_fee(self.db_connection,id_curs,taxa)

    def add_prof(self,nume:str):
        return User.add_prof(self.db_connection,nume)

    def update_prof(self,id_prof:int,nume:str):
        return User.modify_prof(self.db_connection,id_prof,nume)
import tkinter as tk

from src.backend.connection import DBConnection
from src.backend.user import User
from src.frontend.pages.BasePage import BasePage
from src.frontend.pages.LearnersPage import LearnersPage


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
        for F in (LearnersPage,BasePage):
            page_name=F.__name__
            frame=F(parent=self.container,controller=self)
            self.frames[page_name]=frame
            frame.grid(row=0, column=0, sticky="nesw")
        self.show_frame('BasePage')


    def show_frame(self , name):
        frame=self.frames[name]
        frame.tkraise()

    def add_learner(self,nume:str,varsta:int,ocupatie:str,gen:str,email:str):
        return User.introduce_learner(self.db_connection,nume,varsta,ocupatie,gen,email)

    def register_to_course(self,id_cursant:int,id_curs:int):
        return User.register_learner_to_course(self.db_connection,id_cursant,id_curs)

    def unregister_from_course(self,id_cursant:int,id_curs:int,nota_evaluare=3):
        return User.unregister_learner_from_course(self.db_connection,id_cursant,id_curs,nota_evaluare)

    def update_mail(self,id_cursant:int,mail:str):
        return User.update_mail(self.db_connection,id_cursant,mail)
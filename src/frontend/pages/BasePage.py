import tkinter as tk
import random
from tkinter import font as tkfont
import abc
from tkinter.messagebox import showinfo

from src.backend.transactions import Transaction


class BasePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg=parent['bg'])
        self.controller=controller
        self.parent=parent

        self.init_title()
        self.init_buttons()

    @abc.abstractmethod
    def init(self):
        pass

    def init_title(self):
        title_font=tkfont.Font(family='Helvetica',size=20,weight='bold')
        title_color='dark blue'

        title_frame=tk.Frame(master=self,bg=self.parent['bg'])
        title_frame.pack(side=tk.TOP,fill=tk.X)

        title_frame.grid_columnconfigure(0,weight=1)
        tk.Label(master=title_frame,text='MUSIC SCHOOL ',font=title_font,fg=title_color,bg=title_frame['bg']).grid(row=0, column=0, sticky='nesw')

        tk.Button(title_frame,text='⟳',font=title_font,fg=title_color,command=Transaction.end_course(self.controller.db_connection,random.randint(4,10))).grid(row=0,column=1, sticky='ew')

    def init_buttons(self):
        button_font= tkfont.Font(family='Helvetica', size=14)
        buttons_frame=tk.Frame(master=self,bg='gray87')
        buttons_frame.pack(side=tk.TOP, fill=tk.X)

        for i in range(3):
            buttons_frame.grid_columnconfigure(i,weight=1)


        self.button_learners=tk.Button(buttons_frame,text='Learners',font=button_font,command=self.on_learners_button)
        self.button_learners.grid(row=0,column=0,padx=5,pady=5, sticky='ew')

        self.button_courses=tk.Button(buttons_frame,text='Courses',font=button_font,command=self.on_courses_button)
        self.button_courses.grid(row=0,column=1,padx=5,pady=5, sticky='ew')

        self.button_professors=tk.Button(buttons_frame,text='Professors',font=button_font,command=self.on_professors_button)
        self.button_professors.grid(row=0,column=2,padx=5,pady=5, sticky='ew')



    def on_learners_button(self):
        self.controller.show_frame('LearnersPage')

    def on_courses_button(self):
        self.controller.show_frame('CoursesPage')

    def on_professors_button(self):
        self.controller.show_frame('ProfessorsPage')


    def is_mandatory(self,text):
        showinfo(
            title='Information',
            message=text
        )

    def failure(self,text):
        showinfo(
            title='Information',
            message=text
        )

    def succes(self, text):
        showinfo(
            title='Information',
            message=text
        )
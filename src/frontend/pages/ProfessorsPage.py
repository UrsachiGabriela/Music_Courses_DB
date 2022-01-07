import tkinter as tk
from tkinter import ttk
from src.backend.user import User
from src.frontend.pages.BasePage import BasePage
from tkinter.messagebox import showinfo

from src.frontend.utilities.table import TableFrame


class ProfessorsPage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_gui()

    def init_gui(self):
        self.button_professors['bg']='green'

        bg_color='light blue'
        self.viewer_frame = tk.LabelFrame(self, bg=bg_color)
        self.viewer_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.viewer_frame.grid_columnconfigure(0, weight=1)
        self.viewer_frame.grid_columnconfigure(1, weight=1)
        self.viewer_frame.grid_columnconfigure(2, weight=1)
        self.viewer_frame.grid_columnconfigure(3, weight=1)
        self.viewer_frame.grid_rowconfigure(2, weight=1)




        columns_names=['Prof_ID','Name','Course_ID']
        self.table = TableFrame(self.viewer_frame, columns_names)
        self.table.grid(row=2, column=0, columnspan=4, sticky="nesw", padx=5, pady=5)

    def init(self):
        self.init_insert_frame(self.viewer_frame)
        self.init_update_frame(self.viewer_frame)
        self.init_search_frame(self.viewer_frame)


    def init_insert_frame(self,master,row=0,column=0):
        width_label=7

        self.insert_frame=tk.LabelFrame(master, bg='gray85', text='ADD PROFESSOR', fg='dark blue')
        self.insert_frame.grid(row=row, column=column, pady=10)


        name_insert_frame=tk.LabelFrame(self.insert_frame,bg='gray94')
        name_insert_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(name_insert_frame, text='Name: ', bg=name_insert_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.prof_name_insert_entry = tk.Entry(name_insert_frame)
        self.prof_name_insert_entry.grid(row=0, column=1, padx=5, pady=5)


        tk.Button(self.insert_frame, text='Insert', command=self.insert, bg='light cyan',
                  fg='black').grid(row=1, column=0, padx=5, pady=5)


    def init_update_frame(self,master,row=0, column=1):
        width_label = 7

        self.update_frame = tk.LabelFrame(master, bg='gray85', text='UPDATE PROFESSOR', fg='dark blue')
        self.update_frame.grid(row=row, column=column, pady=10)



        id_update_frame=tk.LabelFrame(self.update_frame,bg='gray94')
        id_update_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(id_update_frame, text='ID: ', bg=id_update_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        cmd = f"""
        SELECT id_profesor from profesori
        """
        response=self.controller.db_connection.fetch_data(cmd,[])
        r1=[row[0] for row in response]
        self.id_update_entry=ttk.Combobox(id_update_frame,values=r1)
        self.id_update_entry.grid(row=0, column=1, padx=5, pady=5)




        name_update_frame=tk.LabelFrame(self.update_frame,bg='gray94')
        name_update_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(name_update_frame, text='Name: ', bg=name_update_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.name_update_entry = tk.Entry(name_update_frame)
        self.name_update_entry.grid(row=0, column=1, padx=5, pady=5)


        tk.Button(self.update_frame, text='Update', command=self.update, bg='light cyan',
                  fg='black').grid(row=2, column=0, padx=5, pady=5)



    def init_search_frame(self,master,row=0, column=2):
        width_label = 7
        self.search_frame = tk.LabelFrame(master, bg='gray85', text='SEARCH', fg='dark blue')
        self.search_frame.grid(row=row, column=column, pady=10)

        prof_id_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        prof_id_search_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(prof_id_search_frame, text='Prof ID', bg=prof_id_search_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.prof_id_search_entry = tk.Entry(prof_id_search_frame)
        self.prof_id_search_entry.grid(row=0, column=1, padx=5, pady=5)


        name_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        name_search_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(name_search_frame, text='Name', bg=name_search_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.prof_name_search_entry = tk.Entry(name_search_frame)
        self.prof_name_search_entry.grid(row=0, column=1, padx=5, pady=5)


        tk.Button(self.search_frame, text='Search', command=self.search,bg='light cyan',
                  fg='black').grid(row=2, column=0, padx=5, pady=5)





    def insert(self):
        name=self.prof_name_insert_entry.get().strip()

        if name=='':
            self.failure('Name field is mandatory')
            return

        exec=self.controller.add_prof(name)
        if exec:
            self.succes('Professor successfully added')
        else:
            self.failure('Wrong data inserted')


    def update(self):
        prof_id=self.id_update_entry.get().strip()
        name=self.name_update_entry.get().strip()


        if prof_id=='':
            self.failure('Please select a valid id')
            return

        exec=self.controller.update_prof(prof_id,name)
        if exec:
            self.succes('The prof was successfully changed.')
        else:
            self.failure('Wrong data inserted')


    def search(self):
        prof_id=self.prof_id_search_entry.get().strip()
        name=self.prof_name_search_entry.get().strip()




        if prof_id == '' and name=='' : #afisare tot
            self.populate_the_table_with_all_values()
        elif prof_id =='' and name != '': #cautare dupa nume
            self.search_by_name()
        elif  prof_id != '' and name == '': #cautare dupa id
            self.search_by_id()
        else: #cautare dupa ambele
            self.search_by_name_and_id()

    def search_by_name_and_id(self):
        self.table.clear_table()
        prof_id=self.prof_id_search_entry.get().strip()
        name=self.prof_name_search_entry.get().strip()

        cmd=f"""
            SELECT profesori.id_profesor,nume,id_curs
            FROM profesori,cursuri
            WHERE profesori.id_profesor=cursuri.id_profesor(+)
                AND nume=:n
                AND profesori.id_profesor=:id
                
        """
        response=self.controller.db_connection.fetch_data(cmd,[name,prof_id])
        r=[row for row in response]
        for row in r:
            self.table.insert('', 'end', values=row)


    def search_by_id(self):
        self.table.clear_table()
        prof_id=self.prof_id_search_entry.get().strip()


        cmd=f"""
            SELECT profesori.id_profesor,nume,id_curs
            FROM profesori,cursuri
            WHERE profesori.id_profesor=cursuri.id_profesor
                AND profesori.id_profesor=:id
                 
        """
        response=self.controller.db_connection.fetch_data(cmd,[prof_id])
        r=[row for row in response]
        for row in r:
            self.table.insert('', 'end', values=row)


    def search_by_name(self):
        self.table.clear_table()
        name=self.prof_name_search_entry.get().strip()

        cmd=f"""
            SELECT profesori.id_profesor,nume,id_curs
            FROM profesori,cursuri
            WHERE profesori.id_profesor=cursuri.id_profesor(+)
                AND nume=:n
 
                
        """
        response=self.controller.db_connection.fetch_data(cmd,[name])
        r=[row for row in response]
        for row in r:
            self.table.insert('', 'end', values=row)


    def populate_the_table_with_all_values(self):
        self.table.clear_table()
        cmd=f"""
            SELECT profesori.id_profesor,nume,id_curs
            FROM profesori,cursuri
            WHERE profesori.id_profesor=cursuri.id_profesor(+)

          
        """
        response=self.controller.db_connection.fetch_data(cmd,[])
        r=[row for row in response]
        for row in r:
            self.table.insert('', 'end', values=row)
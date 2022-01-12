import tkinter as tk
from tkinter import ttk
from src.backend.user import User
from src.frontend.pages.BasePage import BasePage
from tkinter.messagebox import showinfo
import re

from src.frontend.utilities.table import TableFrame


class LearnersPage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_gui()

    def init_gui(self):
        self.button_learners['bg']='green'

        bg_color='light blue'
        self.viewer_frame = tk.LabelFrame(self, bg=bg_color)
        self.viewer_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.viewer_frame.grid_columnconfigure(0, weight=1)
        self.viewer_frame.grid_columnconfigure(1, weight=1)
        self.viewer_frame.grid_columnconfigure(2, weight=1)
        self.viewer_frame.grid_columnconfigure(3, weight=1)
        self.viewer_frame.grid_rowconfigure(2, weight=1)




        columns_names=['Learner_ID','Name','Age','Occupation','Gender','Mail','Course_ID','Reg_date','Grade','Reg_fee']
        self.table = TableFrame(self.viewer_frame, columns_names)
        self.table.grid(row=2, column=0, columnspan=4, sticky="nesw", padx=5, pady=5)

    def init(self):
        self.init_register_learner_frame(self.viewer_frame)
        self.init_unregister_frame(self.viewer_frame)
        self.init_update_frame(self.viewer_frame)
        self.init_search_frame(self.viewer_frame)



    def init_register_learner_frame(self,master,row=0,column=0):
        width_label=7
        self.insert_frame=tk.LabelFrame(master, bg='gray85', text='REGISTER TO THE COURSE', fg='dark blue')
        self.insert_frame.grid(row=row, column=column, pady=10)


        id_insert_frame=tk.LabelFrame(self.insert_frame,bg='gray94')
        id_insert_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(id_insert_frame, text='ID: ', bg=id_insert_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        cmd = f"""
         SELECT id_cursant from cursanti
         """
        response=self.controller.db_connection.fetch_data(cmd,[])
        r1=[row[0] for row in response]
        r1.append('New learner')
        self.c_id=tk.StringVar()
        self.c_id.trace('w',self.on_id)
        self.id_insert_entry=ttk.Combobox(id_insert_frame,textvariable=self.c_id,values=r1)
        self.id_insert_entry.grid(row=0, column=1, padx=5, pady=5)



        name_insert_frame=tk.LabelFrame(self.insert_frame,bg='gray94')
        name_insert_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(name_insert_frame, text='Name: ', bg=name_insert_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.learner_name_insert_entry = tk.Entry(name_insert_frame)
        self.learner_name_insert_entry.grid(row=0, column=1, padx=5, pady=5)



        age_insert_frame=tk.LabelFrame(self.insert_frame,bg='gray94')
        age_insert_frame.grid(row=2, column=0, pady=5, padx=5, sticky='w')
        tk.Label(age_insert_frame, text='Age: ', bg=age_insert_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.learner_age_insert_entry = tk.Entry(age_insert_frame)
        self.learner_age_insert_entry.grid(row=0, column=1, padx=5, pady=5)


        occupation_insert_frame=tk.LabelFrame(self.insert_frame,bg='gray94')
        occupation_insert_frame.grid(row=3, column=0, pady=5, padx=5, sticky='w')
        tk.Label(occupation_insert_frame, text='Occupation: ', bg=occupation_insert_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.learner_occupation_insert_entry = tk.Entry(occupation_insert_frame)
        self.learner_occupation_insert_entry.grid(row=0, column=1, padx=5, pady=5)



        gender_insert_frame=tk.LabelFrame(self.insert_frame,bg='gray94')
        gender_insert_frame.grid(row=4, column=0, pady=5, padx=5, sticky='w')
        tk.Label(gender_insert_frame, text='Gender: ', bg=gender_insert_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.learner_gender_insert_entry = tk.Entry(gender_insert_frame)
        self.learner_gender_insert_entry.grid(row=0, column=1, padx=5, pady=5)



        mail_insert_frame=tk.LabelFrame(self.insert_frame,bg='gray94')
        mail_insert_frame.grid(row=5, column=0, pady=5, padx=5, sticky='w')
        tk.Label(mail_insert_frame, text='Mail: ', bg=mail_insert_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.learner_mail_insert_entry = tk.Entry(mail_insert_frame)
        self.learner_mail_insert_entry.grid(row=0, column=1, padx=5, pady=5)


        course_id_insert_frame=tk.LabelFrame(self.insert_frame,bg='gray94')
        course_id_insert_frame.grid(row=6, column=0, pady=5, padx=5, sticky='w')
        tk.Label(course_id_insert_frame, text='Course_ID: ', bg=course_id_insert_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        cmd2 = f"""
         SELECT c.id_curs from cursuri c
         WHERE c.id_curs in (select p.id_curs from program p)
         
         """
        response2=self.controller.db_connection.fetch_data(cmd2,[])
        r2=[row[0] for row in response2]
        self.course_id=tk.StringVar()
        self.course_id_insert_entry=ttk.Combobox(course_id_insert_frame,textvariable=self.course_id,values=r2)
        self.course_id_insert_entry.grid(row=0, column=1, padx=5, pady=5)

    def init_unregister_frame(self,master,row=0, column=1):
        width_label = 7

        self.unregister_frame = tk.LabelFrame(master, bg='gray85', text='UNREGISTER LEARNER', fg='dark blue')
        self.unregister_frame.grid(row=row, column=column, pady=10)



        id_unregister_frame=tk.LabelFrame(self.unregister_frame,bg='gray94')
        id_unregister_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(id_unregister_frame, text='Learner ID: ', bg=id_unregister_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)

        cmd = f"""
        SELECT id_cursant from cursanti
        """
        response=self.controller.db_connection.fetch_data(cmd,[])
        r1=[row[0] for row in response]
        self.id_unregister_entry=ttk.Combobox(id_unregister_frame,values=r1)
        self.id_unregister_entry.grid(row=0, column=1, padx=5, pady=5)




        cmd=f"""
            SELECT distinct id_curs FROM fisa_inscriere
            """

        response=self.controller.db_connection.fetch_data(cmd,[])
        self.courses_list=[row[0] for row in response]

        course_id_unregister_frame=tk.LabelFrame(self.unregister_frame,bg='gray94')
        course_id_unregister_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(course_id_unregister_frame, text='Course ID: ', bg=course_id_unregister_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.course_id_unregister_entry=ttk.Combobox(course_id_unregister_frame,values=self.courses_list)
        self.course_id_unregister_entry.grid(row=0, column=1, padx=5, pady=5)





        tk.Button(self.unregister_frame, text='Unregister', command=self.unregister, bg='light cyan',
                  fg='black').grid(row=2, column=0, padx=5, pady=5)


    def init_update_frame(self,master,row=0, column=2):
        width_label = 7

        self.update_frame = tk.LabelFrame(master, bg='gray85', text='UPDATE MAIL', fg='dark blue')
        self.update_frame.grid(row=row, column=column, pady=10)



        id_update_frame=tk.LabelFrame(self.update_frame,bg='gray94')
        id_update_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(id_update_frame, text='ID: ', bg=id_update_frame['bg'], fg='dark blue',
                     width=width_label).grid(row=0, column=0)
        cmd = f"""
        SELECT id_cursant from cursanti
        """
        response=self.controller.db_connection.fetch_data(cmd,[])
        r1=[row[0] for row in response]
        self.id_update_entry=ttk.Combobox(id_update_frame,values=r1)
        self.id_update_entry.grid(row=0, column=1, padx=5, pady=5)




        mail_update_frame=tk.LabelFrame(self.update_frame,bg='gray94')
        mail_update_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(mail_update_frame, text='Mail: ', bg=mail_update_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.learner_mail_update_entry = tk.Entry(mail_update_frame)
        self.learner_mail_update_entry.grid(row=0, column=1, padx=5, pady=5)


        tk.Button(self.update_frame, text='Update', command=self.update, bg='light cyan',
                      fg='black').grid(row=2, column=0, padx=5, pady=5)


    def init_search_frame(self,master,row=0, column=3):
        width_label = 7
        self.search_frame = tk.LabelFrame(master, bg='gray85', text='SEARCH', fg='dark blue')
        self.search_frame.grid(row=row, column=column, pady=10)

        learner_id_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        learner_id_search_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(learner_id_search_frame, text='Learner ID', bg=learner_id_search_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.learner_id_search_entry = tk.Entry(learner_id_search_frame)
        self.learner_id_search_entry.grid(row=0, column=1, padx=5, pady=5)


        name_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        name_search_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(name_search_frame, text='Name', bg=name_search_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.learner_name_search_entry = tk.Entry(name_search_frame)
        self.learner_name_search_entry.grid(row=0, column=1, padx=5, pady=5)


        tk.Button(self.search_frame, text='Search', command=self.search,bg='light cyan',
                  fg='black').grid(row=2, column=0, padx=5, pady=5)




    #new learner
    def add_learner(self):
        name=self.learner_name_insert_entry.get()
        name=name.strip()

        age=self.learner_age_insert_entry.get()
        age=age.strip()

        occupation=self.learner_occupation_insert_entry.get()
        occupation=occupation.strip()
        occupation=occupation.lower()

        gender=self.learner_gender_insert_entry.get()
        gender=gender.strip()
        gender=gender.upper()

        mail=self.learner_mail_insert_entry.get()
        mail=mail.strip()

        course_id=self.course_id_insert_entry.get().strip()

        if name ==''  or age =='' or course_id =='':
            self.is_mandatory('Name ,Age and CourseID fields are mandatory!')
            return


        is_ok=re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",mail)

        if not is_ok:
            self.failure('Invalid email address')

        exec2=None
        exec1=self.controller.add_learner(name,age,occupation,gender,mail)
        if exec1:
            cmd=f"""
            SELECT max(id_cursant) FROM cursanti
            """
            response=self.controller.db_connection.fetch_data(cmd,[])
            r=[row for row in response]
            r=int(r[0][0]) #id-ul cursantului introdus
            exec2=self.controller.register_to_course(r, course_id)



        if exec1 :
            if exec2:
                self.succes('The learner was successfully registered. Learner ID is ' + str(r))
            else:
                self.succes('The learner was successfully inserted but registration is impossible. Learner ID is ' + str(r))
        else:
            msg=f'Wrong data inserted or mail already exists !\n' \
                f'REMEMBER :\n' \
                f'-nume length must be > 1\n' \
                f'-varsta must be in interval [14,22]\n' \
                f'-ocupatie in (elev,student)\n' \
                f'-gen in (F,M)'

            self.failure(msg)


    # no new learner , only new registration form
    def add_registration_form(self):
        course_id=self.course_id_insert_entry.get().strip()
        learner_id=self.id_insert_entry.get().strip()

        exec=self.controller.register_to_course(learner_id, course_id)
        if exec:
            self.succes('The learner was successfully registered.')
        else:
            self.failure('Wrong data inserted  : \n'
                         ' - this learner is already registered at this course'
                         '                     OR      \n'
                         ' - there are no more seats at the selected course')


    def update(self):
        learner_id=self.id_update_entry.get()
        mail=self.learner_mail_update_entry.get().strip()


        if learner_id=='':
            self.failure('Please select a valid id')
            return

        is_ok=re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",mail)

        if not is_ok:
            self.failure('Invalid email address')
            return

        exec=self.controller.update_mail(learner_id,mail)
        if exec:
            self.succes('The mail was successfully updated.')
        else:
            self.failure('Wrong data inserted or mail already exists!')



    def unregister(self):
        learner_id=self.id_unregister_entry.get().strip()
        course_id=self.course_id_unregister_entry.get().strip()


        cmd=f"""
        SELECT count(*) FROM fisa_inscriere
        WHERE id_curs=:id_c AND id_cursant=:id_cursant 
        """

        response=self.controller.db_connection.fetch_data(cmd,[course_id,learner_id])
        r=[row[0] for row in response]
        r=r[0]

        if(r!=0):
            exec=self.controller.unregister_from_course(learner_id,course_id)
            if(exec):
                self.succes('Unregister done')
            else:
                self.failure('Wrong data inserted')
        else:
            self.failure('The learner is not registered at this course')



    def search(self):
        learner_id=self.learner_id_search_entry.get().strip()
        name=self.learner_name_search_entry.get().strip()



        if learner_id == '' and name=='' : #afisare tot
            self.populate_the_table_with_all_values()
        elif learner_id =='' and name != '': #cautare dupa nume
            self.search_by_name()
        elif  learner_id != '' and name == '': #cautare dupa id
            self.search_by_id()
        else: #cautare dupa ambele
            self.search_by_name_and_id()

    def search_by_name_and_id(self):
        self.table.clear_table()
        learner_id=self.learner_id_search_entry.get().strip()
        name=self.learner_name_search_entry.get().strip()

        cmd=f"""
        SELECT cursanti.id_cursant, nume,varsta,ocupatie,gen,email ,cursuri.id_curs,to_char(data_inscriere,'dd-mon-yy') ,nota_evaluare,
                CASE ocupatie WHEN 'student' THEN taxa_inscriere-0.5*taxa_inscriere
                      WHEN 'elev' THEN taxa_inscriere-0.25*taxa_inscriere
                      ELSE taxa_inscriere
                END
        FROM cursanti ,fisa_inscriere, cursuri ,detalii_cursanti
        WHERE cursanti.id_cursant=fisa_inscriere.id_cursant(+)
            AND cursuri.id_curs(+)=fisa_inscriere.id_curs
            AND cursanti.id_cursant=detalii_cursanti.id_cursant
            AND cursanti.id_cursant=:id_c AND cursanti.nume=:n
        ORDER BY cursanti.id_cursant
        """
        response=self.controller.db_connection.fetch_data(cmd,[learner_id,name])
        r=[row for row in response]
        for row in r:
            self.table.insert('', 'end', values=row)


    def search_by_id(self):
        self.table.clear_table()
        learner_id=self.learner_id_search_entry.get().strip()
        cmd=f"""
        SELECT cursanti.id_cursant, nume,varsta,ocupatie,gen,email, cursuri.id_curs ,to_char(data_inscriere,'dd-mon-yy'),nota_evaluare,
                CASE ocupatie WHEN 'student' THEN taxa_inscriere-0.5*taxa_inscriere
                      WHEN 'elev' THEN taxa_inscriere-0.25*taxa_inscriere
                      ELSE taxa_inscriere
                END
        FROM cursanti ,fisa_inscriere, cursuri ,detalii_cursanti
        WHERE cursanti.id_cursant=fisa_inscriere.id_cursant(+)
            AND cursuri.id_curs(+)=fisa_inscriere.id_curs
            AND cursanti.id_cursant=detalii_cursanti.id_cursant
            AND cursanti.id_cursant=:id_c
        ORDER BY cursanti.id_cursant
        """
        response=self.controller.db_connection.fetch_data(cmd,[learner_id])
        r=[row for row in response]
        for row in r:
            self.table.insert('', 'end', values=row)


    def search_by_name(self):
        self.table.clear_table()
        name=self.learner_name_search_entry.get().strip()
        print(name)
        cmd=f"""
        SELECT cursanti.id_cursant, nume,varsta,ocupatie,gen,email ,cursuri.id_curs,to_char(data_inscriere,'dd-mon-yy') ,nota_evaluare,
                CASE ocupatie WHEN 'student' THEN taxa_inscriere-0.5*taxa_inscriere
                      WHEN 'elev' THEN taxa_inscriere-0.25*taxa_inscriere
                      ELSE taxa_inscriere
                END
        FROM cursanti ,fisa_inscriere, cursuri ,detalii_cursanti
        WHERE cursanti.id_cursant=fisa_inscriere.id_cursant(+)
            AND cursuri.id_curs(+)=fisa_inscriere.id_curs
            AND cursanti.id_cursant=detalii_cursanti.id_cursant
            AND cursanti.nume=:n
        ORDER BY cursanti.id_cursant
        """
        response=self.controller.db_connection.fetch_data(cmd,[name])
        r=[row for row in response]
        for row in r:
            self.table.insert('', 'end', values=row)


    def populate_the_table_with_all_values(self):
        self.table.clear_table()
        cmd=f"""
        SELECT cursanti.id_cursant, nume,varsta,ocupatie,gen,email 
        FROM cursanti ,detalii_cursanti
        WHERE  cursanti.id_cursant=detalii_cursanti.id_cursant
        ORDER BY cursanti.id_cursant
        """

        response=self.controller.db_connection.fetch_data(cmd,[])
        r=[row for row in response]
        for row in r:
            self.table.insert('', 'end', values=row)


    def on_id(self,index, value, op):
        if self.c_id.get() !='New learner':
            self.learner_name_insert_entry.configure(state='disabled')
            self.learner_age_insert_entry.configure(state='disabled')
            self.learner_occupation_insert_entry.configure(state='disabled')
            self.learner_gender_insert_entry.configure(state='disabled')
            self.learner_mail_insert_entry.configure(state='disabled')

            tk.Button(self.insert_frame, text='Insert', command=self.add_registration_form, bg='light cyan',
                      fg='black').grid(row=7, column=0, padx=5, pady=5)
        else:
            self.learner_name_insert_entry.configure(state='normal')
            self.learner_age_insert_entry.configure(state='normal')
            self.learner_occupation_insert_entry.configure(state='normal')
            self.learner_gender_insert_entry.configure(state='normal')
            self.learner_mail_insert_entry.configure(state='normal')

            tk.Button(self.insert_frame, text='Insert', command=self.add_learner, bg='light cyan',
                      fg='black').grid(row=7, column=0, padx=5, pady=5)



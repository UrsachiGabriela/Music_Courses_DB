import tkinter as tk
from tkinter import ttk
from src.backend.user import User
from src.frontend.pages.BasePage import BasePage
from tkinter.messagebox import showinfo

class LearnersPage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_gui()

    def init_gui(self):
        self.button_learners['bg']='green'

        bg_color='light blue'
        viewer_frame = tk.LabelFrame(self, bg=bg_color)
        viewer_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        viewer_frame.grid_columnconfigure(0, weight=1)
        viewer_frame.grid_columnconfigure(1, weight=1)
        viewer_frame.grid_columnconfigure(2, weight=1)
        viewer_frame.grid_columnconfigure(3, weight=1)
        viewer_frame.grid_rowconfigure(2, weight=1)

        self.init_register_learner_frame(viewer_frame)
        self.init_unregister_frame(viewer_frame)
        self.init_update_frame(viewer_frame)

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
        #self.unregister_id=tk.StringVar()
        #self.unregister_id.trace('w',self.on_unregister_id)
        self.id_unregister_entry=ttk.Combobox(id_unregister_frame,values=r1) #********************************************************************
        self.id_unregister_entry.grid(row=0, column=1, padx=5, pady=5)



        self.courses_list=[]
        course_id_unregister_frame=tk.LabelFrame(self.unregister_frame,bg='gray94')
        course_id_unregister_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(course_id_unregister_frame, text='Course ID: ', bg=course_id_unregister_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.course_id_unregister_entry=ttk.Combobox(id_unregister_frame,values=self.courses_list)
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



    #new learner
    def add_learner(self):
        name=self.learner_name_insert_entry.get()
        name=name.strip()

        age=self.learner_age_insert_entry.get()
        age=age.strip()

        occupation=self.learner_occupation_insert_entry.get()
        occupation=occupation.strip()

        gender=self.learner_gender_insert_entry.get()
        gender=gender.strip()

        mail=self.learner_mail_insert_entry.get()
        mail=mail.strip()

        course_id=self.course_id_insert_entry.get().strip()

        if name ==''  or age =='' or course_id =='':
            self.is_mandatory('Name ,Age and CourseID fields are mandatory!')
            return


        exec1=self.controller.add_learner(name,age,occupation,gender,mail)
        if exec1:
            cmd=f"""
            SELECT max(id_cursant) FROM cursanti
            """
            response=self.controller.db_connection.fetch_data(cmd,[])
            r=[row for row in response]
            r=int(r[0][0])
            exec2=self.controller.register_to_course(r, course_id)
        else:
            exec2 = None


        if exec1 :
            if exec2:
                self.succes_insert('The learner was successfully registered. Learner ID is ' + str(r))
            else:
                self.succes_insert('The learner was successfully inserted but registration is impossible. Learner ID is ' + str(r))
        else:
            self.wrong_insert()


    def add_registration_form(self):
        course_id=self.course_id_insert_entry.get().strip()
        learner_id=self.id_insert_entry.get().strip()

        exec=self.controller.register_to_course(learner_id, course_id)
        if exec:
            self.succes_insert('The learner was successfully registered.' )
        else:
            self.wrong_insert()


    def update(self):
        learner_id=self.id_update_entry.get()
        mail=self.learner_mail_insert_entry.get().strip()

        exec=self.controller.update_mail(learner_id,mail)
        if exec:
            self.succes_insert('The mail was successfully updated.' )
        else:
            self.wrong_insert()



    def unregister(self):
        learner_id=self.id_unregister_entry.get().strip()
        #exec=self.controller.






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



    def on_unregister_id(self):
        l_id=self.unregister_id.get()

        cmd=f"""
        SELECT id_curs FROM fisa_inscriere
        WHERE id_cursant=:id
        """

        response=self.controller.db_connection.fetch_data(cmd,[int(l_id)])
        r1=[row[0] for row in response]

        self.courses_list=r1
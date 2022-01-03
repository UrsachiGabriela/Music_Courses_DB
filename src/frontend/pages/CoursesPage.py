import tkinter as tk
from tkinter import ttk
from src.backend.user import User
from src.frontend.pages.BasePage import BasePage
from tkinter.messagebox import showinfo

from src.frontend.utilities.table import TableFrame


class CoursesPage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.init_gui()

    def init_gui(self):
        self.button_courses['bg']='green'

        bg_color='light blue'
        self.viewer_frame = tk.LabelFrame(self, bg=bg_color)
        self.viewer_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.viewer_frame.grid_columnconfigure(0, weight=1)
        self.viewer_frame.grid_columnconfigure(1, weight=1)
        self.viewer_frame.grid_columnconfigure(2, weight=1)
        self.viewer_frame.grid_columnconfigure(3, weight=1)
        self.viewer_frame.grid_rowconfigure(2, weight=1)


        self.init()

        columns_names=['Course_ID','Duration','Instrument','Registr_fee','Max_seats','Free_seats','Prof','Day','Hour','Room']
        self.table = TableFrame(self.viewer_frame, columns_names)
        self.table.grid(row=2, column=0, columnspan=4, sticky="nesw", padx=5, pady=5)
        #self.populate_the_table_with_all_values()


    def  init(self):
        self.init_insert_course_frame(self.viewer_frame)
        self.init_add_program_frame(self.viewer_frame)
        self.init_update_frame(self.viewer_frame)
        self.init_search_frame(self.viewer_frame)

    def init_insert_course_frame(self,master,row=0,column=0):
        width_label=7

        self.insert_frame=tk.LabelFrame(master, bg='gray85', text='ADD COURSE', fg='dark blue')
        self.insert_frame.grid(row=row, column=column, pady=10)



        duration_insert_frame=tk.LabelFrame(self.insert_frame,bg='gray94')
        duration_insert_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(duration_insert_frame, text='Duration:\n (in months)', bg=duration_insert_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.duration_insert_entry = tk.Entry(duration_insert_frame)
        self.duration_insert_entry.grid(row=0, column=1, padx=5, pady=5)


        max_insert_frame=tk.LabelFrame(self.insert_frame,bg='gray94')
        max_insert_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(max_insert_frame, text='Max_seats: ', bg=max_insert_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.max_insert_entry = tk.Entry(max_insert_frame)
        self.max_insert_entry.grid(row=0, column=1, padx=5, pady=5)



        instrument_insert_frame=tk.LabelFrame(self.insert_frame,bg='gray94')
        instrument_insert_frame.grid(row=3, column=0, pady=5, padx=5, sticky='w')
        tk.Label(instrument_insert_frame, text='Instrument: ', bg=instrument_insert_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.instrument_insert_entry = tk.Entry(instrument_insert_frame)
        self.instrument_insert_entry.grid(row=0, column=1, padx=5, pady=5)



        registration_fee_insert_frame=tk.LabelFrame(self.insert_frame,bg='gray94')
        registration_fee_insert_frame.grid(row=4, column=0, pady=5, padx=5, sticky='w')
        tk.Label(registration_fee_insert_frame, text='Fee: ', bg=registration_fee_insert_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.registration_fee_insert_entry = tk.Entry(registration_fee_insert_frame)
        self.registration_fee_insert_entry.grid(row=0, column=1, padx=5, pady=5)



        prof_id_insert_frame=tk.LabelFrame(self.insert_frame,bg='gray94')
        prof_id_insert_frame.grid(row=5, column=0, pady=5, padx=5, sticky='w')
        tk.Label(prof_id_insert_frame, text='Prof_ID: ', bg=prof_id_insert_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        cmd2 = f"""
         SELECT id_profesor from profesori
         
         """
        response2=self.controller.db_connection.fetch_data(cmd2,[])
        r2=[row[0] for row in response2]
        self.prof_id=tk.StringVar()
        self.prof_id_insert_entry=ttk.Combobox(prof_id_insert_frame,textvariable=self.prof_id,values=r2)
        self.prof_id_insert_entry.grid(row=0, column=1, padx=5, pady=5)


        tk.Button(self.insert_frame, text='Add course', command=self.insert_course, bg='light cyan',
                  fg='black').grid(row=6, column=0, padx=5, pady=5)


    def init_add_program_frame(self,master,row=0,column=1):
        width_label = 7
        self.add_prog_frame = tk.LabelFrame(master, bg='gray85', text='ADD PROGRAM', fg='dark blue')
        self.add_prog_frame.grid(row=row, column=column, pady=10)



        course_id_insert_frame=tk.LabelFrame(self.add_prog_frame,bg='gray94')
        course_id_insert_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(course_id_insert_frame, text='Course_ID: ', bg=course_id_insert_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        cmd = f"""
         SELECT id_curs from cursuri
         """
        response=self.controller.db_connection.fetch_data(cmd,[])
        r1=[row[0] for row in response]
        self.course_id=tk.StringVar()
        self.id_insert_entry=ttk.Combobox(course_id_insert_frame,textvariable=self.course_id,values=r1)
        self.id_insert_entry.grid(row=0, column=1, padx=5, pady=5)



        day_insert_frame=tk.LabelFrame(self.add_prog_frame,bg='gray94')
        day_insert_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(day_insert_frame, text='Day: ', bg=day_insert_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.day_insert_entry = tk.Entry(day_insert_frame)
        self.day_insert_entry.grid(row=0, column=1, padx=5, pady=5)


        hour_insert_frame=tk.LabelFrame(self.add_prog_frame,bg='gray94')
        hour_insert_frame.grid(row=2, column=0, pady=5, padx=5, sticky='w')
        tk.Label(hour_insert_frame, text='Hour: ', bg=hour_insert_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.hour_insert_entry = tk.Entry(hour_insert_frame)
        self.hour_insert_entry.grid(row=0, column=1, padx=5, pady=5)



        room_insert_frame=tk.LabelFrame(self.add_prog_frame,bg='gray94')
        room_insert_frame.grid(row=3, column=0, pady=5, padx=5, sticky='w')
        tk.Label(room_insert_frame, text='Room: ', bg=room_insert_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.room_insert_entry = tk.Entry(room_insert_frame)
        self.room_insert_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.add_prog_frame, text='Add program', command=self.add_program, bg='light cyan',
                  fg='black').grid(row=4, column=0, padx=5, pady=5)



    def init_update_frame(self,master,row=0, column=2):
        width_label = 7

        self.update_frame = tk.LabelFrame(master, bg='gray85', text='UPDATE', fg='dark blue')
        self.update_frame.grid(row=row, column=column, pady=10)


        course_id_update_frame=tk.LabelFrame(self.update_frame,bg='gray94')
        course_id_update_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(course_id_update_frame, text='Course ID: ', bg=course_id_update_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        cmd = f"""
        SELECT id_curs from cursuri
        """
        response=self.controller.db_connection.fetch_data(cmd,[])
        r1=[row[0] for row in response]
        self.course_id_update_entry=ttk.Combobox(course_id_update_frame,values=r1)
        self.course_id_update_entry.grid(row=0, column=1, padx=5, pady=5)


        duration_update_frame=tk.LabelFrame(self.update_frame,bg='gray94')
        duration_update_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(duration_update_frame, text='Duration: ', bg=duration_update_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.duration_update_entry = tk.Entry(duration_update_frame)
        self.duration_update_entry.grid(row=0, column=1, padx=5, pady=5)



        reg_fee_update_frame=tk.LabelFrame(self.update_frame,bg='gray94')
        reg_fee_update_frame.grid(row=2, column=0, pady=5, padx=5, sticky='w')
        tk.Label(reg_fee_update_frame, text='Reg_fee: ', bg=reg_fee_update_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.reg_fee_update_entry = tk.Entry(reg_fee_update_frame)
        self.reg_fee_update_entry.grid(row=0, column=1, padx=5, pady=5)


        tk.Button(self.update_frame, text='Update duration', command=self.update_duration, bg='light cyan',
                  fg='black').grid(row=3, column=0, padx=5, pady=5)

        tk.Button(self.update_frame, text='Update reg_fee', command=self.update_reg_fee, bg='light cyan',
                  fg='black').grid(row=3, column=1, padx=5, pady=5)


    def init_search_frame(self,master,row=0, column=3):
        width_label = 7
        self.search_frame = tk.LabelFrame(master, bg='gray85', text='SEARCH', fg='dark blue')
        self.search_frame.grid(row=row, column=column, pady=10)

        course_id_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        course_id_search_frame.grid(row=0, column=0, pady=5, padx=5, sticky='w')
        tk.Label(course_id_search_frame, text='Course ID', bg=course_id_search_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.course_id_search_entry = tk.Entry(course_id_search_frame)
        self.course_id_search_entry.grid(row=0, column=1, padx=5, pady=5)


        instrument_search_frame = tk.LabelFrame(self.search_frame, bg='gray94')
        instrument_search_frame.grid(row=1, column=0, pady=5, padx=5, sticky='w')
        tk.Label(instrument_search_frame, text='Instrument', bg=instrument_search_frame['bg'], fg='dark blue',
                 width=width_label).grid(row=0, column=0)
        self.instrument_search_entry = tk.Entry(instrument_search_frame)
        self.instrument_search_entry.grid(row=0, column=1, padx=5, pady=5)


        tk.Button(self.search_frame, text='Search', command=self.search,bg='light cyan',
                  fg='black').grid(row=2, column=0, padx=5, pady=5)




    def insert_course(self):
        duration=self.duration_insert_entry.get().strip()
        max_seats=self.max_insert_entry.get().strip()
        reg_nr=0
        instrument=self.instrument_insert_entry.get().strip()
        reg_fee=self.registration_fee_insert_entry.get().strip()
        prof_id=self.prof_id_insert_entry.get().strip()



        if duration=='' or max_seats=='' or reg_nr=='' or instrument=='' or reg_fee=='' :
            self.is_mandatory('All fields are mandatory!')
            return

        exec=self.controller.add_course(duration,max_seats,reg_nr,instrument,reg_fee,prof_id)
        if exec:
            self.succes('Course successfully added!')
        else:
            self.failure('Wrong data inserted. Course cannot be inserted')



    def add_program(self):
        course_id=self.course_id.get().strip()
        day=self.day_insert_entry.get().strip()
        hour=self.hour_insert_entry.get().strip()
        room=self.room_insert_entry.get().strip()

        if course_id=='' or day=='' or hour=='' or room=='':
            self.is_mandatory('All fields are mandatory!')
            return

        exec=self.controller.add_add_prog(course_id,day,hour,room)
        if exec:
            self.succes('Program was successfully added!')
        else:
            self.failure('Wrong data inserted. Room/prof busy at this time.')

    def update_duration(self):
        course_id=self.course_id_update_entry.get().strip()
        duration=self.duration_update_entry.get().strip()

        exec=self.controller.update_course_duration(course_id,duration)
        if exec:
            self.succes('Duration successfully updated')
        else:
            self.failure('Duration cannot be modified while course is in progress!')


    def update_reg_fee(self):
        course_id=self.course_id_update_entry.get().strip()
        reg_fee=self.reg_fee_update_entry.get().strip()

        exec=self.controller.update_course_duration(course_id,reg_fee)
        if exec:
            self.succes('Registration fee successfully updated')
        else:
            self.failure('Registration fee cannot be modified while course is in progress!')


    def search(self):
        course_id=self.course_id_search_entry.get().strip()
        instrument=self.instrument_search_entry.get().strip()




        if course_id == '' and instrument=='' : #afisare tot
            self.populate_the_table_with_all_values()
        elif course_id =='' and instrument != '': #cautare dupa nume
            self.search_by_instrument()
        elif  course_id != '' and instrument == '': #cautare dupa id
            self.search_by_id()
        else: #cautare dupa ambele
            self.search_by_instrument_and_id()

    def search_by_instrument_and_id(self):
        self.table.clear_table()
        course_id=self.course_id_search_entry.get().strip()
        instrument=self.instrument_search_entry.get().strip()

        cmd=f"""
            SELECT cursuri.id_curs,durata,instrument,taxa_inscriere,max_locuri,max_locuri-nr_inscrisi,cursuri.id_profesor,zi,to_char(ora,'hh24:mi') ,sala
            FROM cursuri,program,profesori
            WHERE cursuri.id_curs=program.id_curs(+)
                AND cursuri.id_profesor=profesori.id_profesor
                AND cursuri.id_curs=:id_c
                AND instrument=:instr
                
        """
        response=self.controller.db_connection.fetch_data(cmd,[course_id,instrument])
        r=[row for row in response]
        for row in r:
            self.table.insert('', 'end', values=row)


    def search_by_id(self):
        self.table.clear_table()
        course_id=self.course_id_search_entry.get().strip()


        cmd=f"""
            SELECT cursuri.id_curs,durata,instrument,taxa_inscriere,max_locuri,max_locuri-nr_inscrisi,cursuri.id_profesor,zi,to_char(ora,'hh24:mi') ,sala
            FROM cursuri,program,profesori
            WHERE cursuri.id_curs=program.id_curs(+)
                AND cursuri.id_profesor=profesori.id_profesor
                AND cursuri.id_curs=:id_c
                
        """
        response=self.controller.db_connection.fetch_data(cmd,[course_id])
        r=[row for row in response]
        for row in r:
            self.table.insert('', 'end', values=row)


    def search_by_instrument(self):
        self.table.clear_table()
        instrument=self.instrument_search_entry.get().strip()

        cmd=f"""
            SELECT cursuri.id_curs,durata,instrument,taxa_inscriere,max_locuri,max_locuri-nr_inscrisi,cursuri.id_profesor,zi,to_char(ora,'hh24:mi') ,sala
            FROM cursuri,program,profesori
            WHERE cursuri.id_curs=program.id_curs(+)
                AND cursuri.id_profesor=profesori.id_profesor
                AND instrument=:instr
                
        """
        response=self.controller.db_connection.fetch_data(cmd,[instrument])
        r=[row for row in response]
        for row in r:
            self.table.insert('', 'end', values=row)


    def populate_the_table_with_all_values(self):
        self.table.clear_table()
        cmd=f"""
            SELECT cursuri.id_curs,durata,instrument,taxa_inscriere,max_locuri,max_locuri-nr_inscrisi,cursuri.id_profesor,zi,to_char(ora,'hh24:mi') ,sala
            FROM cursuri,program,profesori
            WHERE cursuri.id_curs=program.id_curs(+)
                AND cursuri.id_profesor=profesori.id_profesor
                
        """
        response=self.controller.db_connection.fetch_data(cmd,[])
        r=[row for row in response]
        for row in r:
            self.table.insert('', 'end', values=row)
import tkinter as tk
from tkinter import messagebox
from tkinter import Menu, ttk
from gui.config import GUIConfig
from tkcalendar import Calendar
from pandastable import Table
from core.customers import Customers
from core.table_helper import TableHelper
from gui.menu_helper import MenuHelper
import pandas as pd
from core.data_provider import DataProvider
from core.customer_calendar import CustomerCalendar

class App:
    root = False
    config = False
    role = False
    frame = False

    def __init__(self, root):
        self.root = root
        self.config = GUIConfig()
        self.root.title(self.config.app_title)
        self.debug()
        self.table_helper = TableHelper()
        self.menu_helper = MenuHelper(self.root)
        self.customer_calendar = CustomerCalendar()
        self.dp = DataProvider()

    def set_role(self, role_name='guest'):
        self.role = role_name

    def run(self):
        # self.menu()
        return self.root

    def dispatch_role(self, role_name='guest'):
        role_name  = role_name.lower()

        if role_name == 'admin':
            self.admin()

        elif role_name == 'guest':
            self.guest()

        elif role_name == 'staff':
            self.staff()

        elif role_name == 'member':
            self.member()

        self.role = role_name
        self.menu()

    def admin(self):
        self.frame = self.workbench()
        hone = tk.Label(self.frame, text="Übersicht  Administration").grid(row=0, column=0)
        
        self.table = self.table_helper.get_table(self.frame, 'customer_calendar')
        self.table.grid(row=1, column=2)
        self.table.show()

    def guest(self): # Pouria
        frame = self.workbench()
        my_cal = Calendar(frame,  selectmode="day")
        my_cal.grid(row=2, column=3)

        course_var = tk.StringVar()
        time_var = tk.StringVar()
        trainer_var = tk.StringVar()
        
        dp = DataProvider()
        courses = dp.get_data('courses')
        timeslots = dp.get_data('time_slots')
        trainers = list(dp.get_data('trainers')['trainer'])
        times = list(timeslots['von'].unique())
        
        tk.Label(frame, text="Wähle einen Kurs:").grid(row=3, column=2)
        tk.OptionMenu(frame, course_var, *courses).grid(row=3, column=3)
        tk.Label(frame, text="Wähle eine Uhrzeit:").grid(row=4, column=2)
        tk.Label(frame, text="Wähle einen Trainer:").grid(row=5, column=2)

        course_var.set(courses[0])
        time_var.set(times[0])
        trainer_var.set(trainers[0])

        
        tk.OptionMenu(frame, time_var, *times).grid(row=4, column=3)
        tk.OptionMenu(frame, trainer_var, *trainers).grid(row=5, column=3)

        def book_appointment():
            date = my_cal.get_date()
            course = course_var.get()
            time = time_var.get()
            trainer_name = trainer_var.get()
            tk.messagebox.showinfo("Buchung", f"Termin für {course} am {date} um {time} mit {trainer_name} wurde gebucht!")
            self.customer_calendar.book(c_start=str(date)+' '+time, appt_id=course,member_id=666,c_end=date + '+90', comment=trainer_name)
            self.customer_calendar.save()

        tk.Button(frame, text="Termin buchen", command=book_appointment).grid(row=6, column=3, pady=10)


    def staff(self):
        #tbd
        pass 
        
    def member(self):
        frame = self.workbench()
        my_cal = Calendar(frame,  selectmode="day")
        my_cal.grid(row=2, column=3)

        course_var = tk.StringVar()
        time_var = tk.StringVar()
        trainer_var = tk.StringVar()
        member_id = tk.StringVar()
        
        dp = DataProvider()
        courses = dp.get_data('courses')
        timeslots = dp.get_data('time_slots')
        trainers = list(dp.get_data('trainers')['trainer'])
        times = list(timeslots['von'].unique())
        
        tk.Label(frame, text="Mitglieds-Nr:").grid(row=5, column=5)
        tk.Entry(frame, textvariable=member_id).grid(row=5, column=6)
        
        tk.Label(frame, text="Wähle einen Kurs:").grid(row=3, column=2)
        tk.OptionMenu(frame, course_var, *courses).grid(row=3, column=3)
        tk.Label(frame, text="Wähle eine Uhrzeit:").grid(row=4, column=2)
        tk.Label(frame, text="Wähle einen Trainer:").grid(row=5, column=2)



        course_var.set(courses[0])
        time_var.set(times[0])
        trainer_var.set(trainers[0])

        
        tk.OptionMenu(frame, time_var, *times).grid(row=4, column=3)
        tk.OptionMenu(frame, trainer_var, *trainers).grid(row=5, column=3)

        def book_appointment():
            date = my_cal.get_date()
            course = course_var.get()
            time = time_var.get()
            trainer_name = trainer_var.get()
            member = member_id.get()
            tk.messagebox.showinfo("Buchung", f"Termin von Mitglied {member} für {course} am {date} um {time} mit {trainer_name} wurde gebucht!")
            self.customer_calendar.book(c_start=str(date)+' '+time, appt_id=course,member_id=666,c_end=date + '+90', comment=trainer_name)
            self.customer_calendar.save()

        tk.Button(frame, text="Termin buchen", command=book_appointment).grid(row=6, column=3, pady=10)

    def menu(self):
        content = {
            'Kalender': self.dispatch_cal,
            'Mitglieder': self.dispatch_memb,
            'Trainer': self.dispatch_tr,
            'Zeiten': self.dispatch_time,
            'Buchungen': self.dispatch_customer_calendar,
        }

        menubar = self.menu_helper.get_menu_by_role(self.role, content)

    def debug(self):
        import os

        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)

    def workbench(self):
        ''' “Arbeitstisch„  je Rolle'''

        design = self.config.design_by_role[self.role]

        # nur zum Entwickeln
        frame = tk.Frame(self.root, bg=design[0])
        frame.place(relwidth=1, relheight=1)
        print(self.role.capitalize())
        lbl = tk.Label(frame, text=self.role)
        lbl.grid(row=0, column=0)
        return frame

    def handle_frame(self):
        if self.frame != False:
            self.frame.destroy()
        design = self.config.design_by_role[self.role]
        frame = tk.Frame(self.root, bg=design[0])
        frame.place(relwidth=1, relheight=1)
        return frame

    def dispatch_cal(self):
        print('cal')
        self.frame = self.handle_frame()
        my_cal = Calendar(self.frame, selectmode='day')
        my_cal.grid(row=1, column=1)

    def dispatch_tr(self):
        self.show_objects('trainers')

    def dispatch_time(self):
        self.show_objects('time_slots')
        
    def dispatch_memb(self):
        self.show_objects('customers')
        
    def dispatch_customer_calendar(self):
         self.show_objects('customer_calendar')

    def show_objects(self, topic):
        frame = self.handle_frame()
        print('Topic aus show_objects: ' + topic)
        self.table = self.table_helper.get_table(frame, topic)
        self.table.grid(row=1, column=2)
        self.table.show()

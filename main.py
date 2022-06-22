# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter

import TimeFormatConverter
from ChickIncubationTimer import *
from TimeFormatConverter import *
from HamburgerHamilton import *
from tkinter import *


def calculate_chick_embryo_time(start_day, start_hour, incubation_time):
    day_as_int = get_int_from_days(start_day)
    hour = ChickIncubationTimer.calculate_ending_hour(start_hour, incubation_time)
    day = ChickIncubationTimer.calculate_ending_day(day_as_int, start_hour, hour, incubation_time)
    result_label.config(text=days_to_int[str(day)] + ", " + TimeFormatConverter.get_time_format(hour, 'standard'))


def calculate_from_hamburger_hamilton(start_day, start_hour, hh_stage):
    incubation_time = HamburgerHamilton.get_time_from_stage(hh_stage)
    calculate_chick_embryo_time(start_day, start_hour, incubation_time)


def calculate_time_from_gui():
    time_val = time_to_int(start_time_var.get())
    am_pm_val = start_am_pm.get()
    if am_pm_val == "PM":
        time_val += 12
        if time_val == 24:
            time_val = 12
    else:
        if time_val == 12:
            time_val = 0
    return time_val


def calculate_chick_embryo_time_listener():
    start_time = calculate_time_from_gui()
    inc_time_val = incubation_time_entry.get()
    if inc_time_val == '':
        inc_time_val = 0
    calculate_chick_embryo_time(start_day_var.get(), start_time, int(inc_time_val))


if __name__ == '__main__':
    root = Tk()
    root.title("Chick Incubation Timer Calculator")
    root.config(padx=20, pady=20)
    margin = 0.23

    incubation_start_day_label = Label(root, text="Incubation Start Day", relief=RAISED)
    incubation_start_day_label.grid(row=1, column=0)

    start_day_var = StringVar()
    start_day_var.set("Sunday")
    incubation_start_day = OptionMenu(root, start_day_var, *days_of_week)
    incubation_start_day.grid(row=1, column=1)

    incubation_start_day_label = Label(root, text="Incubation Start Time", relief=RAISED)
    incubation_start_day_label.grid(row=2, column=0)

    start_time_var = StringVar()
    start_time_var.set("12:00")
    incubation_start_time = OptionMenu(root, start_time_var, *available_time)
    incubation_start_time.grid(row=2, column=1)

    incubation_am_pm_label = Label(root, text="AM/PM", relief=RAISED)
    incubation_start_day_label.grid(row=3, column=0)

    start_am_pm = StringVar()
    start_am_pm.set("AM")
    incubation_am_pm = OptionMenu(root, start_am_pm, *am_pm)
    incubation_am_pm.grid(row=3, column=1)

    incubation_time_label = Label(root, text="Total Incubation Time", relief=RAISED)
    incubation_time_label.grid(row=4, column=0)

    incubation_time_entry = Entry(root, text="0")
    incubation_time_entry.grid(row=4, column=1)

    button_calc = Button(root, text="Calculate",
                         command=calculate_chick_embryo_time_listener)
    button_calc.grid(row=5, column=0)

    result_label = Label(root, text="Calculate incubation time")
    result_label.grid(row=5, column=1)
    result_label.config(pady=50)

    root.mainloop()

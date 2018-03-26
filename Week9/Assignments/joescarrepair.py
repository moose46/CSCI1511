__author__ = 'Robert W. Curtiss'
__project__ = 'CS1511'

"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: CS1511
    File: application
    Created: Mar, 26, 2018
    
    Description: Default application class
    
===================================================
"""
from tkinter import *
from tkinter import messagebox

class Repair(object):
    def __init__(self, name, cost):
        self.name = name
        self.is_checked = BooleanVar()
        self.cost = cost


class Application(Frame):
    """
    GUI class with three buttons
    """

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid(sticky=N + E + S + W, padx=15, pady=15)
        self.create_widgets()
        self.root = master

        self.total = 0.0

    def create_widgets(self):

        self.services_frame = LabelFrame(text=" Joe's Services ", padx=10, pady=10, relief=RIDGE, font='Bold')

        self.services_frame.grid(row=0, column=0, padx=20, pady=20, sticky=W)
        self.repairs = []
        self.repairs.append(Repair('Oil Change:', 26))
        self.repairs.append(Repair('Lub Job:', 18))
        self.repairs.append(Repair('Radiator Flush:', 30))
        self.repairs.append(Repair('Transmission Flush:', 80))
        self.repairs.append(Repair('Inspection:', 15))
        self.repairs.append(Repair('Brake Rotors:', 120))
        self.repairs.append(Repair('Muffler Replacement:', 100))
        self.repairs.append(Repair('Tire Rotation:', 20))

        row = 0

        for repair in self.repairs:
            Label(self.services_frame, text=repair.name, font='Bold', fg='Blue').grid(row=row, column=0, sticky=E)
            Checkbutton(self.services_frame,
                        text="${:.2f}".format(repair.cost),
                        variable=repair.is_checked,
                        command=self.update_total,
                        font='Bold', fg='Red'
                        ).grid(row=row, column=1, ipadx=2, ipady=2, sticky=W)
            row += 1
        self.invoice_txt = Text(self.services_frame, width=40, wrap=WORD, font='Bold', bg='Light Yellow')
        self.invoice_txt.grid(row=0, column=2, rowspan=len(self.repairs), sticky=W)
        Button(self.services_frame,
               text='Exit...', font='Bold', command=self.button_exit).grid(row=len(self.repairs) + 1, column=2,
                                                                             padx=10, pady=10, sticky=E)
        self.update_total()

    def button_exit(self):
        messagebox.showinfo("Joe say's, Thanks for visiting...", "Goodbye and thanks for all the fish!")
        self.root.destroy()

    def update_total(self):
        self.total = 0
        txt = "\n\tJoe's Car Repair Invoice\n\n"
        for repair in self.repairs:
            if repair.is_checked.get():
                self.total += repair.cost
                txt += "\t{}\t${:.2f}\n".format(repair.name, repair.cost)
        tax = self.total * 0.06
        self.total += tax
        txt += "\n\tTax (6%): ${:.2f}".format(tax)
        txt += "\n\tTotal Repairs: ${:.2f}".format(self.total)
        self.invoice_txt.delete(0.0, END)
        self.invoice_txt.insert(0.0, txt)


if __name__ == "__main__":
    print("You will need to include this as an import")

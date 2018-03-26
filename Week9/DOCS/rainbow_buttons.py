# Chapter 10 - Project 2
# GUI Grid
# Michael Dawson
# 10/16/06

from tkinter import *

class Application(Frame):
    """ GUI application that creates a grid of buttons. """ 
    COLORS = ['blue', 'green', 'orange', 'red', 'yellow', 'pink', 'cyan', 'magenta']
    color_num = 0
	
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Grid Layout")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create buttons and label with row and column numbers. """
        for row in range(4):
            for column in range(5):
                Application.color_num += 1
                Application.color_num %= len(Application.COLORS)
                text = "row = " + str(row) + "\n" + "column = " + str(column)
                self.bttn = Button(self,
                                   text = text,
                                   font = 38,
                                   bg = Application.COLORS[Application.color_num])
                self.bttn.grid(row = row, column = column)
                ##Button(self, text = text).grid(row = row, column = column)

          
def main():
    app = Application()
    app.mainloop()

main()

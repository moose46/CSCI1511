# Lazy Buttons 2
# Demonstrates using a class with Tkinter

from tkinter import *

class Application(Frame):
    """ A GUI application with three buttons. """ 
    def __init__(self, master):
        """ Initialize the Frame. """
        super(Application, self).__init__(master)    
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create three buttons that do nothing. """
        # create first button
        self.bttn1 = Button(self, text = "I do nothing!",
                            font = 12)

        # create second button
        self.bttn2 = Button(self)
        self.bttn2.configure(text = "Me too!")
        self.bttn2["font"] = 24

        # create third button
        self.bttn3 = Button(self)
        self.bttn3["text"] = "Same here!"
        self.bttn3["font"] = 12

        self.bttn2.grid()	        
        self.bttn3.grid()
        self.bttn1.grid()

# main
def main ():
    root = Tk()
    root.title("Lazy Buttons 2")
    root.geometry("200x300")
    app = Application(root)
    app2 = Application(root)
    root.mainloop()

main()


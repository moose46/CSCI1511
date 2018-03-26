# Labeler
# Demonstrates a label

from tkinter import *

def main():
    # create the root window
    root = Tk()
    root.title("Labeler")
    root.geometry("600x400")

    # create a frame in the window to hold other widgets
    app = Frame(root)
    

    # create a label in the frame
    lbl = Label(app, text = "I'm another label!", font = 8)
    lbl.grid()
    lbl3 = Label(app, text = "I'm in between.", font = 16)
    lbl3.grid()
##    http://www.tutorialspoint.com/python/tk_fonts.htm
    lbl4 = Label(app, text = "It's getting crowded here.", \
                 font = ("Times", 24, "bold italic"))
    lbl4.grid()

    app2 = Frame(root)
    app.grid()
    app2.grid()
    lbl2 = Label(app2, text = "I've been framed!", font = 68)
    lbl2.grid()
    lbl5 = Label(app2, text = "It's getting crowded here.", \
                 font = ("Lucinda", 48, "bold"))
    lbl5.grid()

    # kick off the window's event loop
    root.mainloop()

main()

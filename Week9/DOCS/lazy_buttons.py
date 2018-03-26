# Lazy Buttons
# Demonstrates creating buttons

from tkinter import *

def main():
    # create a root window
    root = Tk()
    root.title("Lazy Buttons")
    root.geometry("800x600")

    # create a frame in the window to hold other widgets
    app = Frame(root)
    app.grid()

    lbl = Label(app, text = "This is just a silly addition.")
    lbl.grid()

    # create a button in the frame
    bttn1 = Button(app, text = "I do nothing!")
    bttn1.grid()

    # create a second button in the frame
    bttn2 = Button(app)

    bttn2.configure(text = "Me too! \n again ...")
    bttn2.configure(font = ("Helvetica", 78))

    # create a third button in the frame
    bttn3 = Button(app)
    bttn3.grid()
    bttn3["text"] = "Same here!"
    bttn3["font"] = ("Arial", 90)
    bttn2.grid()
    # kick off the root window's event loop
    root.mainloop()

main()


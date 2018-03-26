import tkinter
from tkinter import messagebox
from tkinter import *

class testMB():
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.image_frame = tkinter.Frame(self.main_window)
        
        can = tkinter.Canvas(self.image_frame, width = 200, height = 200)
        can.pack()
        img = tkinter.PhotoImage(file = "earth.gif")
        can.create_image((100, 100), image = img) 
      
        # Create the two buttons in the bottom frame
        self.display_button = tkinter.Button(self.top_frame,\
                                text = 'Be nice! Say hello!',\
                                command = self.hello)
        self.quit_button = tkinter.Button(self.bottom_frame,\
                                text = 'Quit',\
                                command =self.main_window.destroy)
              
        # Pack the widgets in the bottom frame
        self.display_button.pack(side='left')
        self.quit_button.pack(side='left')
                
        # Pack the frames
        self.image_frame.pack()
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        self.main_window.mainloop()

    # Define the show_info function
    def hello(self):
                
        # Display message box
        tkinter.messagebox.showinfo(title = "Stubborn", message = "No!!!")
        
        
# Create an instance of AutoGUI
exampleMB = testMB()
                                    

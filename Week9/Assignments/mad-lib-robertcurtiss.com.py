__author__ = 'Robert W. Curtiss'
__project__ = 'Examples'

"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: Examples
    File: mad-lib-robertcurtiss.com
    Created: Mar, 25, 2018
    
    Description:
A story based on user input    
===================================================
"""
from tkinter import *


class Application(Frame):
    """
    GUI class with three buttons
    """

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid(sticky=N + E + S + W, padx=15, pady=15)
        self.create_widgets()
        self.root = master

    def create_widgets(self):
        Label(self,
              text='Enter Information for a new story').grid(row=0,
                                                             column=0,
                                                             columnspan=2,
                                                             sticky=W)
        Label(self,
              text='Person:', width=10, anchor=E, justify=RIGHT).grid(row=1, column=0, sticky=W)
        self.person_ent = Entry(self, textvariable=StringVar(self,value='Bobby'))
        self.person_ent.grid(row=1, column=1, sticky=W)

        Label(self,
              text='Plural Noun:', width=10, anchor=E).grid(row=2, column=0, sticky=W)
        self.noun_ent = Entry(self, textvariable=StringVar(self,value='Cats'))
        self.noun_ent.grid(row=2, column=1, sticky=W)
        Label(self,
              text='Verb:', width=10, anchor=E).grid(row=3, column=0, sticky=W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row=3, column=1, sticky=W)

        Label(self,
              text='Adjectives(s):', width=10, anchor=E).grid(row=4, column=0, sticky=W)

        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text='itchy',
                    variable=self.is_itchy).grid(row=4, column=1, sticky=W)
        self.is_joyous = BooleanVar()
        Checkbutton(self,
                    text='joyous',
                    variable=self.is_joyous).grid(row=4, column=2, sticky=W)
        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text='electric',
                    variable=self.is_electric).grid(row=4, column=3, sticky=W)
        # create label for body parts radio buttons
        Label(self,
              text='Body Part:', width=10, anchor=E).grid(row=5, column=0, sticky=W)
        # create variable for single body part
        self.body_part = StringVar()
        self.body_part.set(None)

        # create body parts radio buttons
        body_parts = ['bellybutton', 'big toe', 'medulla obliongata']
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text=part,
                        variable=self.body_part,
                        value=part).grid(
                row=5, column=column, stick=W)
            column += 1
        # create submit button
        Button(self,
               text='Click for story',
               command=self.tell_story).grid(row=6, column=0, sticky=W)

        self.story_txt = Text(self, width=75, height=10, wrap=WORD)
        self.story_txt.grid(row=7, column=0, columnspan=4)

    def tell_story(self):
        # get values from user input
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        noun = 'cats'
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "itchy "
        if self.is_joyous.get():
            adjectives += "joyous "
        if self.is_electric.get():
            adjectives += "electric "
        body_part = self.body_part.get()

        # create the story
        story = 'The famous explorer '
        story += person
        story += ' had nearly given up a life-long quest to find The Lost City of '
        story += noun.title()
        story += ' when one day, the '
        story += noun
        story += ' found '
        story += person + '.'
        story += ' A strong, '
        story += adjectives
        story += 'peculiar feeling overwhelmed the explorer. '
        story += "After all this time, the quest was finally over. A tear came to "
        story += person + "'s "
        story += body_part + '. '
        story += "And then, the "
        story += noun
        story += ' promptly devoured '
        story += person + '.'
        story += 'The moral of the story? Be careful what you '
        story += verb
        story += " for."


        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)


root = Tk()
root.title = 'Mad Lib pp314'

app = Application(root)

root.mainloop()

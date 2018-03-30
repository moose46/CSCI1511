__author__ = 'Robert W. Curtiss'
__project__ = 'CS1511-27'

from livewires import games, colour
import pygame

"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: CS1511-27
    File: main
    Created: Mar, 29, 2018

    Description: Introducing the Moving Pizza Program pp341
    Using Python2.7, LiveWires 2.1, pygame 1.93  
===================================================
"""
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


# the default is 640x480
# games.Screen().init_screen()

class Pizza(games.Sprite):
    """A pizza sprite"""

    def __init__(self, screen, x, y, image):
        self.init_sprite(screen=screen, x=x, y=y, image=image)

    def moved(self):
        pass


my_screen = games.Screen()

wall_image = games.load_image('images/wall.jpg', transparent=False)
my_screen.set_background(wall_image)

pizza_image = games.load_image('images/pizza.bmp')
Pizza(screen=my_screen, x=SCREEN_WIDTH / 2, y=SCREEN_WIDTH / 2, image=pizza_image)

games.Text(screen=my_screen, x=500, y=30,
           text='Score: 42', size=50, colour=colour.black)
games.Message(screen=my_screen, x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2,
              text='You Won!', size=100, colour=colour.red,
              lifetime=250, after_death=my_screen.quit())
my_screen.mainloop()
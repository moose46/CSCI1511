import random as rnd
import time

__author__ = 'Robert W. Curtiss'
__project__ = 'CS1511'

"""
====================================================
Author: Robert W. Curtiss
Class: CSCI-1511
    Project: CS1511
    File: alien-blaster-robertcurtiss
    Created: Mar, 20, 2018
    
    Description:
    
===================================================
"""


class LifeForm(object):
    die_message = ''
    blast_message = '... {} blasts ...{}! POW!!! - {}\n'

    def __init__(self, name):
        self.name = name
        self.hits = 10
        self.alive = True

    @property
    def is_alive(self):
        return self.alive

    def blast(self, enemy):
        """

        :param enemy: The other LifeForm
        :return: None
        """
        enemy.hits -= 1
        print(self.blast_message.format(self.name, enemy.name, enemy.hits))
        if enemy.hits <= 0:
            print('\n >>>> {} Say''s,  Bang@&! Pow%*@ Bop*%@, I gotcha {}!\n\n'.format(self.name, enemy.name).upper())
            enemy.die()

    def die(self):
        print(self.die_message)
        self.alive = False


class Alien(LifeForm):

    def __init__(self, name):
        super(Alien, self).__init__(name)
        self.die_message = """{}, the alien gasps and says, 'Oh, this is it.  This is the big one.
              Yes, it's getting dark now.  Tell my 1.6 million larvae that I loved them...
              Good-bye, cruel universe.'""".format(self.name)


class Hero(LifeForm):
    def __init__(self, name='Arnold'):
        super(Hero, self).__init__(name)
        self.die_message = """{}, the Hero, dies in his girlfriends arms, sobbing!, no, no, no. :(""".format(self.name)


def main():
    print("\n\t\tDeath of an Alien V2\n")

    hero = Hero()
    # hero.die()

    alien = Alien(name='Zxbirb')
    # alien.die()

    while hero.is_alive and alien.is_alive:
        turn = rnd.randrange(0, 2)
        if turn == 0:
            hero.blast(alien)
        else:
            alien.blast(hero)
        time.sleep(rnd.randrange(1,2))


main()

from unittest import TestCase
from critter import Critter

__author__ = 'Robert W. Curtiss'
__project__ = 'CS1511'



class TestCritter(TestCase):
    # def test_mood(self):
    #     self.fail()
    #
    # def test_talk(self):
    #     self.fail()

    def test_eat(self):
        c = Critter('Bob')
        self.assertEqual(None, c.eat())

    # def test_play(self):
    #     self.fail()

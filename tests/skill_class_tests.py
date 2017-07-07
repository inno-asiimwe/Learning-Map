""" unit tests for the Skill class """

import unittest

from classes import Skill

class Test_Skill_Class(unittest.TestCase):
    """ unit tests for the Skill class """
    def setUp(self):
        """ Initialisation before each test is run """
        self.skill = Skill("HTML")
    def test_init(self):
        """ test the init method of Skill class """
        self.assertEqual("HTML", self.skill.name)
        self.assertFalse(self.skill.studied)

if __name__ == "__main__":
    unittest.main()  

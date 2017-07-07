import unittest
from classes import LearningMap, Skill
 

class TestMap(unittest.TestCase):
    """Doc String for the class"""

    def setUp(self):
        self.map = LearningMap()
        self.skill = Skill('HTML')

    def test_add_skill_success(self):
        """"""
        list_before = len(self.map.skills_list)
        self.map.add_skill('Tdd')
        list_after = len(self.map.skills_list)
        self.assertEqual([list_before, list_after], [0, 1], msg = "skill should be added to the skills_list")

    def test_add_skill_non_string_integer(self):
        """"""
        self.assertRaises(TypeError, self.map.add_skill, 5, msg = "Skill name should be a string")

    def test_add_skill_non_string_list(self):
        """"""
        self.assertRaises(TypeError, self.map.add_skill, ['Tdd', 'HTML'], msg = "Skill name should be a string")

    def test_add_skill_non_string_object(self):
        """"""
        self.assertRaises(TypeError, self.map.add_skill, self.skill, msg = "Skill name should be a string")

if __name__ == '__main__':
    unittest.main()
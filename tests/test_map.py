""" unit tests for LearningMap class"""
import unittest
from classes import LearningMap, Skill
 

class TestMap(unittest.TestCase):
    """Doc String for the class"""

    def setUp(self):
        self.map = LearningMap()
        self.skill = Skill('HTML')

    def test_add_skill_success(self):
        """ tests that skill is added to the skills_list"""
        list_before = len(self.map.skills_list)
        self.map.add_skill('Tdd')
        list_after = len(self.map.skills_list)
        self.assertEqual([list_before, list_after], [0, 1], msg = "skill should be added to the skills_list")

    def test_add_skill_non_string_integer(self):
        """ tests that that skill name should be a string"""
        self.assertRaises(TypeError, self.map.add_skill, 5, msg = "Skill name should be a string")

    def test_add_skill_non_string_list(self):
        """ tests that that skill name should be a string"""
        self.assertRaises(TypeError, self.map.add_skill, ['Tdd', 'HTML'], msg = "Skill name should be a string")

    def test_add_skill_non_string_object(self):
        """ tests that that skill name should be a string"""
        self.assertRaises(TypeError, self.map.add_skill, self.skill, msg = "Skill name should be a string")

    def test_view_learnt_skills(self):
        """ tests that learnt skills have been selected """
        studied_skill = Skill('Css')
        self.assertEqual([studied_skill],self.map.view_skills_not_learnt)

    def test_learnt_skill_string_input(self):
        """Test that skill should be a skill object"""
        self.assertRaises(TypeError, self.map.learnt_skill, 'name')

    def test_learnt_skill_string_integer_input(self):
        """Test that skill should be a skill object"""
        self.assertRaises(TypeError, self.map.learnt_skill, 5)



if __name__ == '__main__':
    unittest.main()
class LearningMap:

    def __init__(self):

        self.skills_list = []
        self.num_learnt_skils = 0
        self.num_skills_not_learnt = 0

    def add_skills(self):
        pass

    def learnt_skill(self, skill):
        if isinstance(skill, Skill):
            if skill.studied :
                return "Skill already attained"
            else:
                skill.studied = True
        else:
            raise TypeError("Skill already attained")
        

    def learning_progress(self):
        pass

    def view_skills_learnt(self):
        pass

    def view_skills_not_learnt(self):
        pass

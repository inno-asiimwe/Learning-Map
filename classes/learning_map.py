class LearningMap:

    def __init__(self):

        self.skills_list = []
        self.num_learnt_skils = 0
        self.num_skills_not_learnt = 0

    def add_skill(self,skill_name):
        pass

        def learnt_skill(self, skill_name):

            if isinstance(skill, Skill):
                if skill.studied:
                    return "Skill already attained"
                else:
                    skill.studied = True
            else:
                raise TypeError("Skill already attained")

        def learning_progress(self):
            pass

        def view_skills_learnt(self):
            if len(self.skills_list) = 0:
                print("No Skills Learnt")
            else:
                for skill in self.skills_list:
                    if skill.studied == True:
                        return skill

        def view_skills_not_learnt(self):
            """ returns the skills not learnt """
            for skill in self.skills_list:
                if skill.studied:
                    pass
                else:
                    print(skill.name)
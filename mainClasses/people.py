from natural_objects import Tear

class Person:
    
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

class Lover(Person):

    def __init__(self, name, sex, pain_lvl):
        super().__init__(name, sex)
        self.tears = [Tear() for lvl in range(pain_lvl)]
        self.criesFor = "No one, yet"
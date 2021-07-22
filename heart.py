import unittest

class Love:

    def __init__(self):
        self.intensity = 0

    def __repr__(self):
        return "Your love intensity is {}".format(self.intensity)

class Heart:

    def __init__(self, age, sex = 3):
        self.sex = sex
        self.age = age
        self.rate = 64

    def isBroken(self):
        if self.rate < 40:
            return True
        else:
            return False

    def __add__(self, other):
        result = Love()
        result.intensity = (self.rate + other.rate) - 120
        return result

class TestHeartMethods(unittest.TestCase):

    def testHeart(self):
        heart = Heart(22)
        self.assertEqual(heart.isBroken(),False)

print(Heart(22) + Heart(19))
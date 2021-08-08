class Drop:
    def __init__(self, width):
        self.height = 50
        self.width = width
        self.isGone = False

    def down(self):
        self.height -= 1
        self.width -= 0.02
        if self.width < 0:
            self.isGone = True

dropA = Drop(.001)
dropB = Drop(1)
dropC = Drop(34)
sky = [dropA, dropB, dropC]

def rain(sky):
    for drop in sky:
        drop.down()
        if drop.isGone:
            return("no splash")

print(rain(sky))

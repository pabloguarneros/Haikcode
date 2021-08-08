class Sky:
    def __init__(self, temp):
        self.temp = temp
        self.drops = []

    def addDrop(self, drop):
        self.drops.append(drop)
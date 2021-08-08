class Coord:

    def __init__(self,x=0,y=0):
        
        self.x = x
        self.y = y

    def __sum__(self, other):

        x_distance = (self.x - other.x)**2
        y_distance = (self.y - other.y)**2

        return ( (x_distance+y_distance) ** (1/2) )

class Entity:

    def __init__(self, coord):
        self.coord = coord

def colorSeen(human, cloud):

    if cloud.coord + human.coord < 5:
        return("grey")

    return("blue")

human_entity = Entity(Coord(1,1))
cloud_entity = Entity(Coord(1,1))

print( f"I see {colorSeen(human_entity, cloud_entity)}" )
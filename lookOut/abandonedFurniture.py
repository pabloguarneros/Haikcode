from mainClasses.people import Person
from mainClasses.human_made_objects import Furniture

pink_cushion = Furniture()
photographer = Person()
wheat_field = Location(#coordinates, #date_time)

def fades():
    dust_level =  pink_cushion.on("wheat-field").dust_level
    if dust_level > 0.2 and dust_level < 0.7:
        photographer.on("car").stays()

pink_cushion.fades()

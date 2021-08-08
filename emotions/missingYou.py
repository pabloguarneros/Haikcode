from mainClasses.people import Person, Lover

def missingYou(me, you):
    for tears in me.tears:
        try:
            me.criesFor = you
            break
        except ValueError:
            print("CriesFor() cannot be set to an object.")

me = Lover('me',0,21)
you = Person('you',0)

missingYou(me, you)

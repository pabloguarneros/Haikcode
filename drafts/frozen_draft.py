def antartica():
    while snow.isFalling():
        mountain.isBuried = True

def antartica_in_spring():
    ice.melts()
    life.begins()

def wave_erupts(force):
    for drop in wave.particles:
        drop.height += randint(0,force*10)

if polar_bear in mother.getChildren():
    polar_bear.follows = mother
    polar_bear.distanceTo(mother) = polar_bear.width * 2.1

def find_novelty_seeking_penguin(waddle):
    waddle.sortBy("dopamine_levels")
    return waddle.pop()

def penguin_mating_call(self):
    self.chest.dips()
    self.grabs_a_rock()

def catch_krill(penguin):
    while penguin.depth > -200 and krill.notSeen():
        penguin.depth -= 1

def catch_krill(humpback):
    for point in krill.radiusPath:
        humpback.blastAir(point)

def find_king_penguin(seal):
    kelp = filter(isKelp,objects_seen)
    penguin = filter(isPenguin,objects_seen)

while bison.isRunning():
    dust.floatsUp()
    bison.tongue.actions.append(waggle)

def macarenia_blooms(self, sunlight):
    if sunlight.reaches(self):
        river_bed.bursts_with_color("red")

class Porous_Rock:
    def __init__(self, fresh_water):
        self.under = fresh_water

def find_freshwater_mammals(season):
    if season == "winter":
        return Manatee()

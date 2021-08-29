def rain(sky):
    for drop in sky:
        drop.down()

def antartica():
    while snow.is_falling():
        mountain.is_buried = True

def antartica_in_spring():
    ice.melts()
    life.begins()

def wave_erupts(force):
    for drop in wave.particles:
        drop.height += randint(0,force*10)

def fire_burns():
    smoke.hangs()
    field.at("sunset").turns("bluish-grey")

def sunset():
    birds.dance()
    sky.set_color("dusted_gold", "pinkish_grey")

def jaggedSnow(mountainRange):
	while snow.isFalling(on=mountainRange.farthestPeak):
		rock.jutOut()



def find_material():
	if “sugar” in ground.description:
		ground.material = Snow()

if ocean.shudders:
    wave.hits("rocky_shores")
    water.append(Particles("scattered_foam"))

while saiga.is_drinking():
    if saiga.is_tense():
        saiga.eyes.look_up()
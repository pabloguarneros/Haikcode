import random


while foam.isVisible:
    wave.retreat()
    I.splash.into["a dream"] = 1
    
def rumble(seconds):
    for s in range(seconds):
        if s % 2:
            earth.position.x += random.randint(0,2)
        else:
            earth.position.x -= random.randint(0,2)

earth.rumble()


if lake.isGlowing:
    camera.setSee(True)

def conqueringFear(person, fear):
    if fear == "height":
        person.climb(getHighestFall([23,12,31,321,31,412,34,12,321,432,321]))

def getHighestFall(mountain_peaks):
    tallest_peak = 0
    highest_fall = 0
    for peak in mountain_peaks:
        if peak.height > tallest_peak:
            tallest_peak = peak.height
        elif tallest_peak - peak.height > highest_fall:
            highest_fall = tallest_peak - peak.height
    return highest_fall
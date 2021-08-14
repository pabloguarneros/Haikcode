def fire_burns():
    smoke.hangs()
    field.at("sunset").turns("bluish-grey")

def horizons():
    for meter in horizon.distance:
        cloud.taperOff(meter)


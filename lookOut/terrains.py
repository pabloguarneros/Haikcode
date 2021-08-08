house = Structure("cube", {'x':2, 'y': 5, 'z': 2} )
hill = terrain.highest_peak
house.on(hill)


if glow.atNight == "casts_a_light":
    night = Time("21:00")
    night.create("a_whisper")

if bus.speeds({"at":"night"}):
    corn.drifts(by = 'two-inches')


if summer_leaves.haveFallen():
    sky.set_to.color("grey")

while air.isMoving():
    thread.fliesAround()
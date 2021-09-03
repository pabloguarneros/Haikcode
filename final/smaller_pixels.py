for particle in air:
    if particle.vibration > 2:
        particle.releases("a_sound")


while flower.is_growing():
    petal.starts_forming()
    petal.awaits("bloom")

for neuron in nervous_system:
    for _ in range(3):
        body.create("glia_cell")
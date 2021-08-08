class Smell:

    def __init__(self):
        self.particles = [ [0 for i in range(5)] for j in range(5)]
        self.spread_speed = 20

    def isSniffed(self, snif_force, nostril_size):
        if snif_force > 0:
            print("none")

    def getTailHeight(self, particle):
        if particle:
            return max(self.getTailHeight(particle.left),self.getTailHeight(particle.right)) + 1
        else:
            return 0

#diffusion of particles through air
#odour particles move freely in air
#olfactory bulb where chemical composition is determined
#--> connected to amygdala (emotion) and hippocampus
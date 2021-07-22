def birdFlight(bird, sky, house):

    if sky.is_bright:
        bird.can_fly()

    if house.has_glass:
        bird.can_die()

    return bird.rate_of_survival
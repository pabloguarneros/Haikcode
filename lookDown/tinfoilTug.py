def tinfoilTug(pigeons):
    while len(pigeons) > 1:
        tinfoilTug( sortByGrip(pigeons) )
    return pigeons #a pigeon

def sortByGrip(birds):
    return birds[:-2]
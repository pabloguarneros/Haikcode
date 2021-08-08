def checkIfSame(flowerOne, flowerTwo):
    for petal_index in range(len(flowerOne)):
        if flowerOne[petal_index] != flowerTwo[petal_index]:
            return False

def heartBeat(time, I, leaves):
    if time.isStill():
        I.die(until=leaves.changeColor("green","black"))
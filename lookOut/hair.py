class hairStrand():

    def __init__(self, strand_size):
        self.strand = [i/strand_size for i in range(strand_size)]
    
class hair():

    def __init__(self, hair_strands):
        self.strand_list = [hairStrand(10) for i in range(hair_strands)] 

    def runFingers(self, position):
        if position%2 == 0:
            self.strand_list #changes probability

blondeHair = hair(110,000)

blondeHair.runFingers(1) #position between  0-13
[   1 , 2,
    3,4,
    5,6,
    7,8,
    9,10,
    11,12,
    13,14 ]
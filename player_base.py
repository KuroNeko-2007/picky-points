import numpy as np
import numpy.typing as npt
# numpy is useful for handling of large arrays, so it is imported here
# numpy.typing is imported since Snehil likes to use type annotations


class Player:
    def __init__(self, name: str):
        self.name = name

    def think(self, points: npt.NDArray[np.float64]):
        ######################################################
        ################ Write your code here ################
        ######################################################


        return point # numpy array of size (1, 3)
    

######################################
######## Give your bot a name ########
######################################

player = Player("Test Bot v1.0.0")
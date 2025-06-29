############################################
#### Example of a bot created by Snehil ####
#### It just picks a random point       ####
############################################


import numpy as np
import numpy.typing as npt
# numpy is useful for handling of large arrays, so it is imported here
# numpy.typing is imported since Snehil likes to use type annotations


class Player:
    def __init__(self, name: str):
        self.name = name

    def think(self, points: npt.NDArray[np.float64]):
        point = np.random.random(3) * 16

        return point # numpy array of length 3
    

player = Player("Snehil's Random Bot v1.0.0")
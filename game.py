import numpy as np
import numpy.typing as npt

class Game:
    radius_sq: float = 1
    points: npt.NDArray[np.float64]

    def __init__(self, point_count: int, max_coord: float, dimension: int = 3):
        self.points = np.random.random((point_count, dimension)) * max_coord
        self.max_coord = max_coord
        self.dimension = dimension
        self.init_point_count = point_count


    def _in_sphere(self, point: npt.NDArray[np.float64]):
        return np.sum(point**2) <= self.radius_sq


    def choose(self, center: npt.NDArray[np.float64]):
        score = 0
        indices = []
        for i in range(0, len(self.points)):
            if self._in_sphere(self.points[i] - center):
                score += 1
                indices.append(i)
        
        self.points = np.delete(self.points, indices, axis=0)
        return score

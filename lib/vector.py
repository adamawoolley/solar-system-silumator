from dataclasses import dataclass
from math import sqrt

@dataclass
class vector():
    x: float
    y: float
    z: float

    def distanceto(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

    def __add__(self, other):
        if isinstance(other, vector):
            return vector(self.x + other.x, self.y + other.y, self.z + other.z)

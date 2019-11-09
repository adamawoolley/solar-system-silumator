from dataclasses import dataclass
from typing import ClassVar
from lib.variables import grav_const
from math import sqrt

@dataclass
class body():
    mass: float
    radius: float
    position: ClassVar # vector
    velocity: ClassVar # vector
    acceleration: ClassVar # vector
    surface_map: str
    grav_const: int = 6.67408e-11

    def update_position(self):
        pass

    def update_velocity(self, gravity):
        pass

    def calculate_gravity(self, other):
        distance = self.position.distanceto(other.position)
        return self.grav_const*((self.mass*other.mass)/distance**2)

    def update(self, bodies):
        '''
        Calculate the gravitational force
        exerted by the other bodies in the
        system in order to update velocity
        '''
        for obj in bodies:
            if obj not self:
                self.update_velocity(calculate_gravity(obj))
        self.update_position()

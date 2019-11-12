from vpython import *
from time import sleep

class system():
    def __init__(self, deltat=0.005, rate=100, *args):
        self.bodies = args
        self.deltat = deltat
        self.rate = rate

    def run(self):
        while True:
            for body in self.bodies:
                body.update_position(self.bodies, self.deltat)
            sleep(self.rate)
            
class celectialObject():
    def __init__(self, pos=vector(0,0,0), radius=10, color=color.orange, velocity=vector(0,0,0), mass=10, name="george"):
        self.sphere = sphere(pos=pos, radius=radius, color=color)
        self.velocity = velocity
        self.mass = mass
        self.name = name

    def distance_to(self, other):
        return sqrt((self.sphere.pos.x - other.sphere.pos.x)**2 \
                  + (self.sphere.pos.y - other.sphere.pos.y)**2 \
                  + (self.sphere.pos.z - other.sphere.pos.z)**2)

    def unit_vector_to(self, other):
        return (other.sphere.pos - self.sphere.pos)/self.distance_to(other)

    def calculate_gravity(self, other):
        print(self.name, "to", other.name, self.unit_vector_to(other))
        return self.unit_vector_to(other) * (6.673e-11*((self.mass*other.mass)/self.distance_to(other)**2))

    def update_position(self, bodies, deltat):
        acceleration = vector(0,0,0)
        for body in bodies:
            if body != self:
                acceleration += self.calculate_gravity(body)
        print(self.name, "acc", acceleration)
        self.velocity += acceleration * deltat
        print(self.name, "Pos", self.sphere.pos)
        self.sphere.pos += self.velocity * deltat

if __name__ == '__main__':

    sun = celectialObject(pos=vector(0,0,0), radius=695510, color=color.orange, velocity=vector(0,0,0), mass=1.9885e30, name='sun')

    mercury = celectialObject(pos=vector(57.9e6,0,0), radius=4879/2*100, color=color.green, velocity=vector(0,47.4,0), mass=0.33e24, name='mercury')

    s = system(0.5, 5, sun, mercury)

    s.run()
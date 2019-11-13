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
                body.update_position(self.bodies, self.deltat, self.rate)
            rate(self.rate)
            #sleep(self.rate)
            
class celectialObject():
    def __init__(self, pos=vector(0,0,0), radius=10, color=color.orange, velocity=vector(0,0,0), mass=10, name="george"):
        self.sphere = sphere(pos=pos, radius=radius, color=color, make_trail=True, retain=50)
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

    def update_position(self, bodies, deltat, rate):
        acceleration = vector(0,0,0)
        for body in bodies:
            if body != self:
                acceleration += self.calculate_gravity(body)/self.mass
        print(self.name, "acc", acceleration)
        self.velocity += acceleration * (deltat / rate)
        print(self.name, "Pos", self.sphere.pos)
        self.sphere.pos += self.velocity * (deltat / rate)

if __name__ == '__main__':

    sun = celectialObject(pos=vector(0,0,0), radius=695510*2, color=color.orange, velocity=vector(0,0,0), mass=1.9885e30, name='sun')

    mercury = celectialObject(pos=vector(-57.9e6,0,0), radius=4879/2*200, color=color.green, velocity=vector(0,-47.5e4*3,0), mass=0.33e24, name='mercury')

    venus = celectialObject(pos=vector(108.2e6,0,0), radius=12104/2*200, color=color.cyan, velocity=vector(0,35.0e4*3,0), mass=4.87e24, name='venus')

    earth = celectialObject(pos=vector(0,149.6e6,0), radius=12756/2*200, color=color.blue, velocity=vector(-29.8e4*3,0,0), mass=5.97e24, name='earth')

    moon = celectialObject(pos=vector(0,149.6e6 + 0.384e6,0), radius=3475/2*200, color=color.yellow, velocity=vector(1.0e4*3,0,0), mass=0.073e24, name='moon')

    s = system(100, 400, sun, mercury, venus, earth, moon)

    s.run()
from vpython import *

global G
G = 6.673e-11

class system():
    def __init__(self, *args, deltat=0.005, rate=100):
        self.bodies = args
        self.deltat = deltat
        self.rate = rate

    def run(self):
        while True:
            for body in self.bodies:
                body.update_position(self.bodies, self.deltat)
            rate(self.rate)

class celectial_object():
    def __init__(self, pos=vector(0,0,0), radius=10, color=color.orange, velocity=vector(0,0,0), mass=10):
        self.sphere = sphere(pos=pos, radius=radius, color=color)
        self.velocity = velocity
        self.mass = mass

    def distanceto(self, pos, other):
        return sqrt((pos.x - other.x)**2 + (pos.y - other.y)**2 + (pos.z - other.z)**2)

    def calculate_unit_vector(self, pos, other):
        return (pos - other)/self.distanceto(pos, other)

    def calculate_gravity(self, pos, other):
        distance = self.distanceto(pos, other.sphere.pos)
        unit_vector = self.calculate_unit_vector(pos, other.sphere.pos)
        return unit_vector * (G*((self.mass*other.mass)/distance**2))

    def update_position(self, bodies, deltat):
        future = self.sphere.pos + self.velocity * deltat
        acceleration = vector(0,0,0)
        for body in bodies:
            if body != self:
                current_acceleration = self.calculate_gravity(self.sphere.pos, body)
                future_acceleration = self.calculate_gravity(future, body)
                acceleration += (current_acceleration + future_acceleration)/2
        self.velocity += acceleration
        self.sphere.pos += self.velocity * deltat

sun = celectial_object(pos=vector(0,0,0), radius=16, color=color.orange, velocity=vector(0,0,0), mass=20)

planet = celectial_object(pos=vector(-100,0,0), radius=4, color=color.green, velocity=vector(0,0,0), mass=5)

s = system(sun, planet, deltat=0.005, rate=10)

s.run()

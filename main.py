from vpython import *

class system():
    def __init__(self, *args, deltat=0.005, rate=100):
        self.bodies = args
        self.deltat = deltat
        self.rate = 100

    def run(self):
        while True:
            for body in self.bodies:
                body.pos += body.velocity * self.deltat
            rate(self.rate)

sun = sphere(pos=vector(0,0,0), radius=10,color=color.orange)
sun.velocity = vector(0,0,0)
sun.mass = 100

planet = sphere(pos=vector(-100,0,0), radius=5, color=color.green, make_trail=True)
planet.velocity = vector(100,100,0)
planet.mass = 50


s = system(sun, planet)

s.run()
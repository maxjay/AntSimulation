import numpy as numpy
import random

class Ant():
    def __init__(self):
        self.angle = random.random() * numpy.pi * 2
        self.speed = 0.1
        self.x = 0
        self.y = 0
        self.timeAlive = 0
        self.targetAngle = random.random() * 2 * numpy.pi
        self.turnRate = 0
        self.rotate()

    def move(self):
        self.x += self.speed * numpy.cos(self.angle)
        self.y += self.speed * numpy.sin(self.angle)
        self.angle = (self.angle + self.turnRate) % (numpy.pi * 2)
        # self.angle = self.angle + (self.targetAngle - self.angle) * 0.005
        if abs(self.targetAngle - self.angle) < 0.02:
            self.rotate()

    def rotate(self):
        self.targetAngle = random.random() * numpy.pi * 2
        diff = self.targetAngle - self.angle
        if diff < 0:
            diff += 2 * numpy.pi
        if diff > numpy.pi:
            self.turnRate = -0.01 / (random.random() + 1)
        else:
            self.turnRate = 0.01 / (random.random() + 1)

    def update(self):
        self.move()
        self.timeAlive += 1

# def rotate(self):
# class Home():
#     def __init__(self):
#         pass

# class Food():
#     def __init__(self):
#         pass

# class Pheromone():
#     def __init__(self):
#         self.radius
#         self.halflife
#         self.type
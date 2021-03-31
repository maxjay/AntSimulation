import math
import random

class Ant():
    def __init__(self):
        self.angle = random.random() * math.pi
        # self.angle = math.pi
        self.speed = 0.01
        self.x = 0
        self.y = 0
        self.timeAlive = 0

    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        # print(self.x, self.y)

    def update(self):
        self.move()
        if self.timeAlive % 100 == 0:
            self.rotate()
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


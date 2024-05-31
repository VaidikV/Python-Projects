from turtle import Turtle, colormode
import random

colormode(255)

COLORS = [(26, 109, 163), (193, 39, 81), (237, 161, 51), (234, 215, 86),
          (222, 138, 176), (142, 109, 58), (102, 197, 218), (205, 165, 30), (21, 58, 132), (211, 74, 91),
          (237, 89, 52), (142, 208, 226), (119, 191, 140), (6, 158, 88), (5, 186, 179), (106, 108, 198)]

starting_speed = 3


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(random.randint(-300, 15000), random.randint(-245, 250))

    def move_car(self):
        self.backward(starting_speed)


def increase_speed():
    global starting_speed
    starting_speed += 4

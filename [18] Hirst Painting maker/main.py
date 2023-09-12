import turtle as t
import random

t.colormode(255)

# import colorgram
#
# colors = colorgram.extract('damien-hirst-spot-painting.jpg', 20)
# col_list = []
#
# for color in colors:
#     color_tuple = (color.rgb[0], color.rgb[1], color.rgb[2])
#     col_list.append(color_tuple)

color_list = [(26, 109, 163), (193, 39, 81), (237, 161, 51), (234, 215, 86),
              (222, 138, 176), (142, 109, 58), (102, 197, 218), (205, 165, 30), (21, 58, 132), (211, 74, 91),
              (237, 89, 52), (142, 208, 226), (119, 191, 140), (6, 158, 88), (5, 186, 179), (106, 108, 198)]

pat = t.Turtle()
pat.width(20)
pat.hideturtle()
pat.speed(0)


def next_line():
    pat.setheading(90)
    pat.penup()
    pat.forward(80)
    pat.setheading(180)
    pat.forward(560)
    pat.setheading(0)


def million_painting():
    for _ in range(7):
        pat.pendown()
        pat.dot(40, random.choice(color_list))
        pat.penup()
        pat.forward(80)
        pat.pendown()
    next_line()


pat.penup()
pat.setheading(220)
pat.forward(320)
pat.setheading(0)

for number in range(6):
    million_painting()

screen = t.Screen()
screen.exitonclick()

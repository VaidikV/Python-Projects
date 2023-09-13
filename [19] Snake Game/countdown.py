from turtle import Turtle
import time


class CountDown(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.counter()

    def counter(self):
        # The way I used range here is also used in the snake code to make the snake move.
        for n in range(3, 0, -1):
            self.write(arg=n, align="center", font=("Courier", 65, "normal"))
            time.sleep(1)
            self.clear()

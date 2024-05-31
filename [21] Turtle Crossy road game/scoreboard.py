from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-220, 260)
        self.display_score()

    def display_score(self):
        self.write(arg=f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def update_score(self):
        self.clear()
        self.level += 1
        self.display_score()

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Courier", 30, "normal"))


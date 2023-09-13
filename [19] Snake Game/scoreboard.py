from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 18, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears whatever that was written earlier and then displays a fresh new scoreboard.
        It happens so quickly that we can't even notice it."""

        self.clear()
        self.goto(0, 270)
        self.write(arg=f"score = {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def high_score_updater(self):
        """If the current player-score is > than the previous high-score(in the txt file), then the original
        high-score txt is replaced with the current high-score."""

        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
            self.update_scoreboard()
            self.celebration()

    def celebration(self):
        """Lets the player know that they made a new high-score by writing a text just below the score-board."""
        self.goto(0, 250)
        self.penup()
        self.color("white")
        self.write(arg="You made a new High Score!", align=ALIGN, font=("Courier", 15, "normal"))

    def game_over(self):
        """Lets the player know that the game is over by displaying a giant message."""
        self.goto(0, 0)
        self.penup()
        self.color("white")
        self.write(arg="GAME OVER", align=ALIGN, font=("Courier", 30, "normal"))

    def score_printer(self):
        """This adds a point in the score and then updates the score-board to show the live score of the
        player. This should be ideally used after each time the snake eats the food."""
        self.score += 1
        self.update_scoreboard()

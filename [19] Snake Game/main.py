from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from countdown import CountDown

# Make the actual screen where the game will be displayed.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Let the player choose the Difficulty level.
user_choice = screen.textinput(title="Choose Difficulty",
                               prompt="What difficulty level do you want? (easy / normal / hard / expert)")
levels = ["easy", "normal", "hard", "expert"]
# Refer line 44 for more info about the items in the list below.
speeds = [0.1, 0.09, 0.05, 0.03]
difficulty = levels.index(user_choice)

# Turn animation OFF (0)
screen.tracer(0)

# Make Objects necessary for the game.
countdown = CountDown()
snake = Snake()
food = Food()
score = ScoreBoard()

# Let the player move the snake using the arrow keys.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Boolean to stop the game when needed.
game_is_on = True

while game_is_on:
    # update displays the animation as a still frame at that particular moment.
    screen.update()
    # Sleep pauses the screen for the amount of time which you mentioned.
    # The lower the time, the quicker the snake will seem to move.
    # Here, sleep is necessary because this is a while loop and the screen will update awfully quicker...making the
    # snake as fast as flash XD
    time.sleep(speeds[difficulty])
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        snake.extend()
        score.score_printer()
        food.refresh()
        score.high_score_updater()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.high_score_updater()
        score.game_over()
        game_is_on = False

    # Detect collision with tail.
    # Here we have split the list "segment" to start with the element in position 2 (3rd element in the list.)
    # This is to prevent the game from stopping everytime as the second segment is always going to be at a
    # distance less than 10.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.high_score_updater()
            score.game_over()
            game_is_on = False

screen.exitonclick()

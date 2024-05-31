from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
score = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detect collision with the wall
    if ball.ycor() > 284 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.l_paddle_bounce_x()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.r_paddle_bounce_x()

    if ball.xcor() > 460:
        ball.lost()
        score.l_point()

    if ball.xcor() < -460:
        ball.lost()
        score.r_point()

screen.exitonclick()

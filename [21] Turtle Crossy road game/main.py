import time
from turtle import Screen
from player import Player
from car_manager import CarManager, increase_speed
from scoreboard import Scoreboard

game_is_on = True
all_cars = []

# Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Cross")
screen.tracer(0)
screen.listen()

# Build  objects
timmy = Player()
score = Scoreboard()

for car_index in range(500):
    car = CarManager()
    all_cars.append(car)

# Make the turtle move by pressing the "Up" button
screen.onkeypress(timmy.move, "Up")

while game_is_on:
    time.sleep(0.01)
    screen.update()
    for cars in all_cars:
        if timmy.distance(cars) < 23:
            game_is_on = False
            score.game_over()
        if timmy.ycor() > 300:
            timmy.level_up()
            increase_speed()
            score.update_score()
        cars.move_car()

screen.exitonclick()

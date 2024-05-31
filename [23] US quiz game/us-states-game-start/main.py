import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
learn = data.state.to_list()
all_x = data.x.to_list()
all_y = data.y.to_list()

answer_counter = 0
correct_answers = []


def make_turtle():
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.goto(all_x[all_states.index(state)], all_y[all_states.index(state)])
    new_turtle.write(arg=f"📍{state}", font=("helvetica", 10, "normal"))


def update_score():
    global answer_counter
    answer_counter += 1


game_on = True

while game_on:
    user_answer = screen.textinput(title=f"{answer_counter}/50 States Correct",
                                   prompt="What's another state's name").title()

    if user_answer == "Exit":
        useful_data = pandas.DataFrame(learn)
        useful_data.to_csv("states_to_learn.csv")
        break

    for state in all_states:
        if user_answer == state and user_answer not in correct_answers:
            correct_answers.append(user_answer)
            learn.remove(user_answer)
            print(len(learn))
            print(correct_answers)
            make_turtle()
            update_score()

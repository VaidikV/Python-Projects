from flask import Flask
import random

app = Flask(__name__)

user_guess = 0
random_number = 0


@app.route("/")
def home_route():
    global random_number
    random_number = random.randint(0, 9)
    return '<h1>Guess a number between 0 and 9</h1>' \
        # '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:num>")
def user_choice(num):
    global random_number
    if num == random_number:
        return "<h1 style='color: green'>You found me! Go back to the home page to play again.</h1>" \
            # "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='found-me'>"
    elif num < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
            # "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h1 style='color: orange'>Too high, try again!</h1>" \
            # "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
language_word = ""
english_word = ""
current_card = {}
to_learn = {}
# ---------------------------- CSV SETUP/ FILES MAKING / CHECKING ------------------------------- #

# Reading the csv file using pandas
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # Converting the dataframe to a dictionary.
    to_learn = data.to_dict(orient="records")


# ---------------------------- CARD FLIPPING ------------------------------- #
# --- CHOOSING A RANDOM WORD FUNCTION --- #
def pick_random():
    global current_card
    global language_word, english_word
    language_word = ""
    english_word = ""
    current_card = random.choice(to_learn)
    language_word = current_card["French"]
    english_word = current_card["English"]


# Flip the card
def flip():
    # Changing card theme
    image_holder.config(file="images/card_back.png")
    # Changing title and word and their font colour as well
    canvas.itemconfig(language_name, text="English", fill="White")
    canvas.itemconfig(raw_word, text=english_word, fill="White")


# ---------------------------- NEXT WORD ------------------------------- #

# --- Known button pressed --- #
def known():
    to_learn.remove(current_card)
    new_df = pandas.DataFrame(to_learn)
    new_df.to_csv("data/words_to_learn.csv", index=False)
    next_word()


def next_word():
    global flip_timer
    pick_random()
    window.after_cancel(flip_timer)
    # Changing card theme
    image_holder.config(file="images/card_front.png")
    # Changing title and word and their font colour as well
    canvas.itemconfig(language_name, text=data.columns[0], fill="Black")
    canvas.itemconfig(raw_word, text=language_word, fill="Black")
    # Flipping the card
    flip_timer = window.after(3000, flip)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip)

# Canvas (front)
canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
image_holder = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 265, image=image_holder)
language_name = canvas.create_text(400, 150, text="", font=("arial", 40, "italic"))
raw_word = canvas.create_text(400, 263, text="", font=("Arial", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong = PhotoImage(file="images/wrong.png")  # assigning the tkinter PhotoImage to the variable
wrong_button = Button(image=wrong, relief="flat",  # relief makes the border of the button disappear
                      bg=BACKGROUND_COLOR, command=next_word)  # superimposing the assigned image on the button
wrong_button.grid(row=1, column=0)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, relief="flat", bg=BACKGROUND_COLOR, command=known)
right_button.grid(row=1, column=1)

# Running the app
next_word()

window.mainloop()

from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Label
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 15))
        self.score.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.quote = self.canvas.create_text(
            150,
            125,
            width=280,
            fill=THEME_COLOR,
            text="Nintendo started out as a playing card manufacturer.",
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        right = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right, bd=0, highlightthickness=0, relief="flat", command=self.true_button_pressed)
        self.right_button.grid(row=2, column=0)

        wrong = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong, bd=0, highlightthickness=0, relief="flat", command=self.false_button_pressed)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quote, text=q_text)
            self.buttons_state(ACTIVE)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quiz!")
            self.buttons_state(DISABLED)

    def true_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score.config(text=f"Score: {self.quiz.score}")
            self.buttons_state(DISABLED)
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def buttons_state(self, state: str):
        self.right_button.config(state=state)
        self.wrong_button.config(state=state)

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
RED = "#ec524b"
BLUE = "#577A8B"
CREAM = "#f5f5f5"
GREEN = "#6AAD5C"
FONT_NAME = "Helvetica"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark_adder = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # Make the start button active again
    start["state"] = "normal"
    # Stop the timer
    window.after_cancel(timer)
    # Reset the timer to 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # Reset the title to Pomodoro Timer
    title.config(text="Pomodoro Timer", fg=RED)
    # Reset the checkmarks
    checkmarks.config(text="")
    global checkmark_adder
    checkmark_adder = ""
    # Reset the reps
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start["state"] = "disabled"
    # start["disabledforeground"] = start["foreground"] Make the button appear that it can be pressed.
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Long Break", fg=BLUE)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Short Break", fg=BLUE)
    else:
        count_down(work_sec)
        title.config(text="Work", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global checkmark_adder
    count_min = math.floor(count / 60)  # can also do count // 60
    count_sec = count % 60

    if count_sec in range(10):
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
        start_timer()
        if reps % 2 == 0:
            checkmark_adder += "✔"
            checkmarks.config(text=f"{checkmark_adder}")
    # ---------------------------- UI SETUP ------------------------------- #


# Window
window = Tk()
window.title("Pomodoro Timer")  # Tomato in Italian
window.config(padx=50, pady=20, bg=CREAM)
window.attributes('-topmost', 0)
# Icon
window.iconbitmap("alarm_clock_icon.ico")

# Canvas:
canvas = Canvas(width=230, height=230, bg=CREAM, highlightthickness=0)
clock_img = PhotoImage(file="alarm-clock.png")
canvas.create_image(115, 115, image=clock_img)
canvas.create_rectangle(70, 70, 160, 150, fill=CREAM, outline=CREAM)
timer_text = canvas.create_text(115, 123, text="00:00", fill=RED, font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Label:
title = Label(text="Pomodoro Timer", fg=RED, bg=CREAM, width=14, font=(FONT_NAME, 45, "bold"))
title.config(pady=40)
title.grid(column=1, row=0)

checkmarks = Label(fg=GREEN, bg=CREAM, font=(FONT_NAME, 17, "bold"))
checkmarks.grid(column=1, row=3)

# Buttons:
start = Button(text="Start", command=start_timer, font=(FONT_NAME, 15, "bold"), fg=GREEN)
start.grid(column=0, row=2)

reset = Button(text="Reset", command=reset_timer, font=(FONT_NAME, 15, "bold"), fg=RED)
reset.grid(column=2, row=2)

window.mainloop()

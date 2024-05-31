from tkinter import *

FONT = ("Helvetica", 18)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=30, pady=30)

# Entry widget:
miles = Entry(width=10)
miles.grid(column=1, row=0)

# Label widget:
label1 = Label(text="Miles", font=FONT)
label1.grid(column=2, row=0)
label1.config(padx=10, pady=10)

label2 = Label(text="is equal to", font=FONT)
label2.grid(column=0, row=1)
label2.config(padx=10, pady=10)

label3 = Label(text=0, font=FONT)
label3.grid(column=1, row=1)
label3.config(padx=10, pady=10)

label4 = Label(text="Km", font=FONT)
label4.grid(column=2, row=1)
label4.config(padx=10, pady=10)


# Button Action:
def convert():
    converted_number = round(int(miles.get()) * 1.609, 2)
    label3.config(text=converted_number)


# Button widget:
calc_button = Button(text="Calculate", command=convert)
calc_button.grid(column=1, row=2)
calc_button.config(padx=5, pady=5)

window.mainloop()

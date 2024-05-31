from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = ("helvetica", 10, "bold")
RED = "#E63F3A"
YELLOW = "#FF9A00"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Making 3 lists containing random elements from the specified list mentioned above in the form of list compression.
    random_letters = [choice(letters) for _ in range(randint(8, 10))]
    random_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    random_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    pass_list = random_letters + random_numbers + random_symbols

    # Randomizing the list and then converting it to a string.
    shuffle(pass_list)
    # Converts the list into a string and puts "" (basically nothing.You can put anything tho) in between every element.
    password = "".join(pass_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    fetch_website = website_entry.get()
    fetch_email_username = email_entry.get()
    fetch_password = password_entry.get()
    new_data = {
        fetch_website: {
            "email": fetch_email_username,
            "password": fetch_password
        }
    }
    if len(fetch_website) == 0 or len(fetch_password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            if fetch_website in data:
                already = messagebox.askyesno(title="Warning",
                                              message=f"Password for {fetch_website} is already stored. "
                                                      f"Do you want to overwrite it?")
                if already:
                    # Updating old data with new data
                    data.update(new_data)
                    with open("data.json", "w") as data_file:
                        # Saving updated data
                        json.dump(data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
        finally:
            # Deleting the contents of website, email & password and inserting the default email again.
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(0, "vaid.ik.vvv@gmail.com")


# ---------------------------- FIND PASSWORD MECHANICS ------------------------------- #
def find_password():
    the_website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            read = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found!")
    else:
        if the_website in read:
            username_from_json = read[the_website]["email"]
            password_from_json = read[the_website]["password"]
            messagebox.showinfo(title=the_website,
                                message=f"Username = {username_from_json}\nPassword = {password_from_json}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {the_website} exists.")


# ---------------------------- WEBSITES ADDED BUTTON MECHANISM ------------------------------- #
sites_added = ""


def show_run():

    with open("data.json") as data_file:
        data = json.load(data_file)
        global sites_added
        sites_added = ""
        for site in data:
            sites_added += f"{site}      \n"


def show_list():
    show_run()
    messagebox.showinfo(title="Websites added", message=sites_added)


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# For changing the icon for the window
window.iconbitmap("lock.ico")

# Canvas
canvas = Canvas(width=250, height=200)
logo = PhotoImage(file="password.png")
canvas.create_image(148, 85, image=logo)
canvas.grid(column=1, row=0, sticky=EW)

# Labels
website = Label(text="Website:", font=FONT)
website.grid(column=0, row=1, sticky=E)
website.config(pady=10)

email_username = Label(text="Email / Username:", font=FONT)
email_username.grid(column=0, row=2, sticky=E)

password_list = Label(text="Password:", font=FONT)
password_list.grid(column=0, row=3, sticky=E)
password_list.config(pady=10)

# Entries
website_entry = Entry(width=41)
website_entry.grid(row=1, column=1, columnspan=2, sticky=W)
website_entry.focus()

email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
email_entry.insert(0, "vaid.ik.vvv@gmail.com")

password_entry = Entry(width=41)
password_entry.grid(row=3, column=1, sticky=W)

# Buttons
generate_password = Button(text="GENERATE PASSWORD", command=password_generator, font=FONT,
                           fg="White", bg=RED)
generate_password.grid(row=3, column=2, sticky=EW)

add = Button(text="ADD", command=save, font=FONT, fg="white", bg=YELLOW)
add.grid(row=4, column=1, columnspan=2, sticky=EW)

search = Button(text="SEARCH", command=find_password, font=FONT, fg="White", bg=RED)
search.grid(row=1, column=2, sticky=EW)

websites_added = Button(text="WEBSITES ADDED", command=show_list, font=FONT, fg="White", bg=YELLOW)
websites_added.grid(row=5, column=1, columnspan=2, sticky=EW)
window.mainloop()

from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import string
import pyperclip
import json


# Functions
def generate_password():
    alpha = string.ascii_lowercase + string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    password = [choice(alpha) for _ in range(randint(8, 10))] + \
               [choice(symbols) for _ in range(randint(8, 10))] + \
               [choice(numbers) for _ in range(randint(8, 10))]
    shuffle(password)
    password_entry.delete(0, END)
    password_entry.insert(0, ''.join(password))
    pyperclip.copy(''.join(password))


def add():
    credentials = {
        website_entry.get(): {
            "Username": username_entry.get(),
            "Password": password_entry.get()
        }
    }
    if len(website_entry.get()) == 0 or len(username_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Oops..", message="Make sure to fill in all the information!")
    else:
        is_ok = messagebox.askokcancel(title="Password Manager", message=f"The new credentials is:\n"
                                                                         f"{website_entry.get()}\n"
                                                                         f"User: {username_entry.get()}\n"
                                                                         f"Password: {password_entry.get()}")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(credentials, data_file, indent=4)
            else:
                data.update(credentials)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)


def search():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError as error:
        messagebox.showinfo(title="Error", message=f"{error}")
    else:
        if website_entry.get() in data:
            messagebox.showinfo(title=f"{website_entry.get()}",
                                message=f"Username: {data[website_entry.get()]['Username']}\n"
                                        f"Password: {data[website_entry.get()]['Password']}")
        else:
            messagebox.showinfo(title=f"{website_entry.get()}",
                                message=f"No such entry for {website_entry.get()}")


# UI
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries

website_entry = Entry()
website_entry.focus()
website_entry.grid(column=1, row=1)

username_entry = Entry(width=38)
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

# Buttons

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1)

window.mainloop()

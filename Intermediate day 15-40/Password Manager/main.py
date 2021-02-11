from tkinter import *
from tkinter import messagebox
import random
import string


# Functions
def generate_password():
    alpha = string.ascii_lowercase + string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    password = ''
    
    for letter in range(0, 10):
        password += random.choice(alpha)
    for symbol in range(0, 10):
        password += random.choice(symbols)
    for number in range(0, 10):
        password += random.choice(numbers)
    shuffled_pass = list(password)
    random.shuffle(shuffled_pass)
    password_entry.insert(0, ''.join(shuffled_pass))


def add():
    if len(website_entry.get()) == 0 or len(username_entry.get()) == 0 or len(password_entry.get()):
        messagebox.showinfo(title="Oops..", message="Make sure to fill in all the information!")
    else:
        is_ok = messagebox.askokcancel(title="Password Manager", message=f"The new credentials is:\n"
                                                                         f"{website_entry.get()}\n"
                                                                         f"User: {username_entry.get()}\n"
                                                                         f"Password: {password_entry.get()}")
        if is_ok:
            with open("data.txt", 'a') as data:
                data.write(f"{website_entry.get()} | Username: {username_entry.get()} | Password: {password_entry.get()}\n")
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)


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

website_entry = Entry(width=38)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry(width=38)
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

# Buttons

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

# ---------------------------- Libraries ------------------------------- #
from tkinter import *
import pandas
from random import choice


# ---------------------------- GLOBALS ------------------------------- #
to_learn = {}
current_card = {}

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

try:
    DATA = pandas.read_csv('data/Words_to_learn.csv')
except FileNotFoundError:
    DATA = pandas.read_csv('data/he-ru.csv')
    to_learn = DATA.to_dict(orient="records")
else:
    to_learn = DATA.to_dict(orient="records")


# ---------------------------- FUNCTIONS ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    print(current_card["Hebrew"])
    canvas.itemconfig(card_title, text="עִברִית", fill="black")
    canvas.itemconfig(card_word, text=current_card["Hebrew"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="русский", fill="white")
    canvas.itemconfig(card_word, text=current_card["Russian"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)


def is_known():
    to_learn.remove(current_card)

    data = pandas.DataFrame(to_learn)
    data.to_csv('data/Words_to_learn.csv', index=False)

    next_card()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

card_cross_img = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=card_cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

card_check_img = PhotoImage(file='images/right.png')
known_button = Button(image=card_check_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()

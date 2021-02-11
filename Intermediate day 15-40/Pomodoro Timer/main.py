from tkinter import *
from math import floor
from win10toast import ToastNotifier

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHEK_MARK = "✔"


# ---------------------------- GLOBALS ------------------------------- #
reps = 0
marks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global marks, reps
    marks = ""
    reps = 0
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text=marks)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_mechanism():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown_mechanism(long_break_sec)
        title_label.config(text="Long Break!", fg=RED)
        notification("Long Break!")
    elif reps % 2 == 0:
        countdown_mechanism(short_break_sec)
        title_label.config(text="Short Break!", fg=PINK)
        notification("Short Break!")
    else:
        countdown_mechanism(work_sec)
        title_label.config(text="Work!", fg=GREEN)
        notification("Work!")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown_mechanism(count):
    count_min = floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, countdown_mechanism, count - 1)
    else:
        timer_mechanism()

        if reps % 2 == 0:
            global marks
            marks += CHEK_MARK
            check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
def notification(text):
    notificator.show_toast('Pomodoro!', f'{text}', duration=10, threaded=True)


window = Tk()
window.title("Pomodoro")
window.config(padx=10, pady=10, bg=YELLOW)

notificator = ToastNotifier()


canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="pomodoro.png")
canvas.create_image(150, 150, image=img)
timer_text = canvas.create_text(150, 130, text="00:00", font=(FONT_NAME, 48, "bold"), fill="white")
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", height=1, width=10, highlightthickness=0, command=timer_mechanism)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", height=1, width=10, highlightthickness=0, command=timer_reset)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
check_mark.grid(column=1, row=3)

window.mainloop()

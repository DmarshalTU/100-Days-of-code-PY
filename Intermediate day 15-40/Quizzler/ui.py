from tkinter import *
from tkinter import messagebox

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0",
                                 fg="white",
                                 bg=THEME_COLOR,
                                 font=("Ariel", 14, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=400, height=400, bg="white")
        self.question_text = self.canvas.create_text(200, 200,
                                                     width=350,
                                                     text="question text",
                                                     fill=THEME_COLOR,
                                                     font=("Ariel", 24, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        try:
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        except IndexError:
            messagebox.showinfo(title="END", message=f"Out of questions\nYour score is {self.quiz.score}/10")
            self.canvas.config(bg="white")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

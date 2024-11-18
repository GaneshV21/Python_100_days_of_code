import tkinter
from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_text=Label(text="Score : 0",fg="white",bg=THEME_COLOR)
        self.score_text.grid(row=0,column=1)

        self.canvas= Canvas(width=300,height=250,bg="white")
        self.inner_text=self.canvas.create_text(150,125,width=280,text="Some Question Text",font=("Ariel",20,'italic'),fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2,padx=20,pady=20)

        self.correct_image=PhotoImage(file='./images/true.png')
        self.button_correct=Button(image=self.correct_image,highlightthickness=0,command=self.true_func)
        self.button_correct.grid(row=2,column=0)

        self.wrong_image = PhotoImage(file='./images/false.png')
        self.button_wrong = Button(image=self.wrong_image,highlightthickness=0,command=self.false_func)
        self.button_wrong.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.question=self.quiz.next_question()
            self.canvas.itemconfig(self.inner_text,text=f"{self.question}")
        else:
            self.canvas.itemconfig(self.inner_text,text="You've reached the end of the quiz. ")
            self.button_correct.config(state="disabled")
            self.button_wrong.config(state="disabled")




    def true_func(self):
        if(self.quiz.check_answer("True")):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_text.config(text=f"Score : {self.quiz.score}")
        self.get_next_question()
        self.window.after(1000,self.normal_bg)

    def normal_bg(self):
        self.canvas.config(bg="white")

    def false_func(self):
        if(self.quiz.check_answer("False")):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_text.config(text=f"Score : {self.quiz.score}")
        self.get_next_question()
        self.window.after(1000,self.normal_bg)






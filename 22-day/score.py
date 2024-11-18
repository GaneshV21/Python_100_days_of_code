
from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial", 24, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score1=0
        self.score2=0
        self.penup()
        self.color("white")
        self.goto(0,250)
        self.write(f"Score : {self.score1} Vs {self.score2}", align=ALIGNMENT,font=FONT)
        self.hideturtle()

    #message after the game
    def message(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT,font=FONT)

    #for detecting left side score
    def left_increase_score(self):
        self.score1+=1
        self.clear()
        self.write(f"Score : {self.score1} Vs {self.score2}", align=ALIGNMENT, font=FONT)

    # for detecting right side score
    def right_increase_score(self):
        self.score2+=1
        self.clear()
        self.write(f"Score : {self.score1} Vs {self.score2}", align=ALIGNMENT, font=FONT)

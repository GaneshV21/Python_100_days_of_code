from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open('file.txt') as file:
            self.high_score = int(file.read())
        self.penup()
        self.color("white")
        self.goto(0,210)
        self.write(f"Score : {self.score} High Score: {self.high_score}", align=ALIGNMENT,font=FONT)
        self.hideturtle()

    #to reset score to - score =0 and maintain high score
    def reset(self):
        self.clear()
        if self.score>self.high_score:
            self.high_score=self.score
            with open('file.txt', mode='w') as file:
                file.write(f"{self.high_score}")
            self.score=0
        self.write(f"Score : {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    #display game over message not needed
    def message(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT,font=FONT)

    #for every food snake score increased
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


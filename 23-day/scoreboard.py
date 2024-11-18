FONT = ("Courier", 24, "normal")
ALIGNMENT="center"
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-220, 220)
        self.write(f"level {self.level}", align=ALIGNMENT, font=FONT)

    def game_level(self):
        self.level+=1
        self.clear()
        self.write(f"level {self.level}",align=ALIGNMENT,font=FONT)


    def game_over(self):
        message = Turtle()
        message.hideturtle()
        message.penup()
        message.color("black")
        message.goto(0,0)
        message.write("Game Over.",align="center",font=FONT)


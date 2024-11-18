STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
ALIGNMENT="center"
FONT=("Arial", 24, "normal")
from turtle import Turtle


class Player():
    def __init__(self):
        super().__init__()
        self.player=[]
        self.create()
        self.level=1

    def move(self):
        self.player[0].forward(MOVE_DISTANCE)

    def create(self):
        player=Turtle("turtle")
        player.penup()
        player.setheading(90)
        player.goto(STARTING_POSITION)
        self.player.append(player)



    def next_level(self):
        self.player[0].goto(STARTING_POSITION)





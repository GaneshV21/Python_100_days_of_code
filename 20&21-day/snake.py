from turtle import Turtle
class Snake():
    def __init__(self):
        self.segment=[]
        self.x=0
        self.y=0
        self.create()
        self.head=self.segment[0]

    #to reset snake position to (0,0) and create new snake
    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.x = 0
        self.y = 0
        self.create()
        self.head = self.segment[0]

    #to create new snake
    def create(self):
        for _ in range(3):
            timmy = Turtle("square")
            timmy.penup()
            timmy.goto(self.x, self.y)
            self.x -= 20
            timmy.color("white")
            self.segment.append(timmy)

    #for moving snake
    def snake_move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    #snake movements
    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    #snake size changes
    def next_size(self):
        timmy = Turtle("square")
        timmy.penup()
        x_value=self.segment[len(self.segment)-1].xcor()
        y_value=self.segment[len(self.segment)-1].ycor()
        timmy.goto(x_value-20,y_value)
        timmy.color("white")
        self.segment.append(timmy)





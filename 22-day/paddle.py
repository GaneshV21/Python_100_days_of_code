from turtle import Turtle
import random
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.arr = []
        self.x=350
        self.y=0
        self.z=-350
        self.a=0
        self.create()
        self.ball()

    #create two paddle
    def create(self):
        paddle1 = Turtle("square")
        paddle2= Turtle("square")
        paddle1.penup()
        paddle2.penup()
        paddle1.goto(self.x, self.y)
        paddle2.goto(self.z, self.a)
        paddle1.color("white")
        paddle2.color("white")
        paddle1.shapesize(stretch_wid=5, stretch_len=1)
        paddle2.shapesize(stretch_wid=5, stretch_len=1)
        self.arr.append(paddle1)
        self.arr.append(paddle2)

    #up down w s function for mooving paddle
    def up(self):
        if self.y != 250:
            self.y+=50
            self.arr[0].goto(self.x,self.y)

    def down(self):
        if self.y != -250:
            self.y-=50
            self.arr[0].goto(self.x,self.y)

    def W(self):
        if self.a != 250:
            self.a+=50
            self.arr[1].goto(self.z,self.a)

    def S(self):
        if self.a != -250:
            self.a-=50
            self.arr[1].goto(self.z,self.a)

    #creating a ball
    def ball(self):
        ball=Turtle("circle")
        ball.color("white")
        ball.speed("slowest")
        self.arr.append(ball)

    #function for ball move
    def ball_move(self):
        self.arr[2].penup()
        ran_left=random.randint(0,45)
        ran_right=random.randint(180,225)
        ran=random.randint(45,180)
        #changing random direction if the ball goes top and down
        if self.arr[2].ycor()<-280:
            self.arr[2].setheading(ran)
        elif self.arr[2].ycor()>280:
            self.arr[2].setheading(-ran)

        #detecting the ball touch the paddle
        elif self.arr[0].distance(self.arr[2])<40:
            self.arr[2].setheading(ran_right)
        elif self.arr[1].distance(self.arr[2])<40:
            self.arr[2].setheading(ran_left)
        self.arr[2].forward(0.3)






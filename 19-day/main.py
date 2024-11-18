# from turtle import Turtle,Screen
# timmy=Turtle()
# screen = Screen()
# screen.listen()
# def forwards():
#     timmy.forward(10)
# def backwards():
#     timmy.backward(10)
#
# def clear():
#     timmy.home()
#     timmy.clear()
# def clockwise():
#     timmy.setheading(0)
#
# def left():
#     head=timmy.heading()+10
#     timmy.setheading(head)
#
#
# def right():
#     head = timmy.heading() - 10
#     timmy.setheading(head)
#
#
# def counter_clockwise():
#     timmy.setheading(180)
#
# screen.onkey(key="w",fun=forwards)
# screen.onkey(key="s",fun=backwards)
# screen.onkey(key="c",fun=clear)
# screen.onkey(key="d",fun=clockwise)
# screen.onkey(key="a",fun=counter_clockwise)
# screen.onkey(key="l",fun=left)
# screen.onkey(key="r",fun=right)
# screen.exitonclick()


#project
from turtle import Turtle,Screen
import random
is_race_on=False
screen = Screen()
screen.setup(width=500,height=400)
user_choice=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors=["red","orange","yellow","green","blue","purple"]
x=-230
y=-90

all_turtles=[]
for color in colors:
    timmy = Turtle(shape="turtle")
    timmy.color(color)
    timmy.penup()
    timmy.goto(x,y)
    y+=30
    all_turtles.append(timmy)


if user_choice:
    is_race_on=True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            if user_choice==turtle.pencolor():
                print(f"You've won! The {turtle.pencolor()} turtle is the winner!")
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle is the winner!")
            is_race_on=False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()



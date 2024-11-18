import turtle
from turtle import Turtle

timmy= Turtle()
# timmy.shape("turtle")
# timmy.color("red")

#first challege
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#

#second challenge
# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

#third challenge
# for _ in range(3):
#     timmy.color("red")
#     timmy.right(120)
#     timmy.forward(100)
#
# for _ in range(4):
#     timmy.color("blue")
#     timmy.right(90)
#     timmy.forward(100)
#
# for _ in range(5):
#     timmy.color("green")
#     timmy.right(72)
#     timmy.forward(100)
#
# for _ in range(6):
#     timmy.color("yellow")
#     timmy.right(60)
#     timmy.forward(100)
#
#
# for _ in range(7):
#     timmy.color("black")
#     timmy.right(51.43)
#     timmy.forward(100)
#
#
#
# for _ in range(8):
#     timmy.color("brown")
#     timmy.right(45)
#     timmy.forward(100)
#
#
# for _ in range(9):
#     timmy.color("pink")
#     timmy.right(40)
#     timmy.forward(100)
#
# for _ in range(10):
#     timmy.color("orange")
#     timmy.right(36)
#     timmy.forward(100)


#fourth challenge
# import random
# direction=[0,90,180,270]
#
# def get_color():
#     tu1 = random.randint(0, 255)
#     tu2 = random.randint(0, 255)
#     tu3 = random.randint(0, 255)
#     tup = (tu1 / 255, tu2 / 255, tu3 / 255)
#     return tup
#
#
# for _ in range(100):
#     timmy.color(get_color())
#     timmy.setheading(random.choice(direction))
#     timmy.pensize(5)
#     timmy.speed("fastest")
#     timmy.forward(15)

#fifth challenge
# timmy.speed("fastest")
# import random
# def get_color():
#     tu1 = random.randint(0, 255)
#     tu2 = random.randint(0, 255)
#     tu3 = random.randint(0, 255)
#     tup = (tu1 / 255, tu2 / 255, tu3 / 255)
#     return tup
#
# def draw(size):
#     for _ in range(int(360/size)):
#         timmy.color(get_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading()+size)
#
# draw(5)

#final painting

# import colorgram
#
# colors=colorgram.extract("images.jpg",30)
# col=[]
# for i in range(len(colors)):
#     r=colors[i].rgb.r
#     g=colors[i].rgb.g
#     b=colors[i].rgb.b
#     tup=(r,g,b)
#     col.append(tup)
# print(col)
import random
turtle.colormode(255)
timmy.penup()
timmy.hideturtle()
color_list=[(228, 222, 214), (185, 167, 154), (236, 222, 229), (224, 235, 227), (129, 94, 63), (225, 230, 238), (18, 23, 48), (215, 201, 146), (186, 153, 164), (45, 21, 14), (67, 94, 125), (144, 165, 184), (143, 178, 157), (211, 183, 178), (135, 73, 92), (49, 14, 27), (167, 15, 45), (173, 148, 62), (52, 124, 86), (11, 38, 20), (198, 94, 75), (199, 80, 99), (218, 176, 187), (45, 55, 99), (170, 206, 186), (76, 158, 109), (144, 30, 22), (12, 99, 62), (241, 221, 3), (186, 187, 208)]
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.speed("fastest")
for _ in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)








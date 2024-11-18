COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
class CarManager():
    def __init__(self):
        super().__init__()
        self.car_arr=[]
        self.car_speed=MOVE_INCREMENT

    def Create(self):
        random_choice=random.randint(1,6)
        if random_choice==1:
            car=Turtle("square")
            car.penup()
            car.goto(300, random.randint(-250,280))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(COLORS[random.randint(0,len(COLORS)-1)])
            self.car_arr.append(car)

    def Move(self):
        for car in self.car_arr:
            # car.setheading(180)
            # car.forward(MOVE_INCREMENT)
            car.backward(self.car_speed)

    def levelup(self):
        self.car_speed+=MOVE_INCREMENT



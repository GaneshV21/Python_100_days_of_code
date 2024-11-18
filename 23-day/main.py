import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
player=Player()
game_is_on = True
scoreboard=Scoreboard()

screen.onkey(player.move,key="Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.Create()
    car_manager.Move()
    if player.player[0].ycor()>280:
        player.next_level()
        car_manager.levelup()
        scoreboard.game_level()
    for car in car_manager.car_arr:
        if car.distance(player.player[0])<20:
            scoreboard.game_over()
            game_is_on=False


screen.exitonclick()

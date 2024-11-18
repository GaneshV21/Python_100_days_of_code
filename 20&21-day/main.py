from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
scoreboard=Scoreboard()
screen.setup(width=600,height=500)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake=Snake()
food=Food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    #if snake hits their body
    for i in range(1,len(snake.segment)):
        if snake.head.distance(snake.segment[i])<10:
            scoreboard.reset()
            # game_is_on=False
            snake.reset()

    #if snake hits cornors
    if (snake.head.xcor()>270 or snake.head.xcor()<-270) or (snake.head.ycor()>220 or snake.head.ycor()<-220):
        scoreboard.reset()
        # game_is_on=False
        snake.reset()

    else:
        #snake moving
        snake.snake_move()

        #snake hits food random food again come
        if snake.head.distance(food)<15:
            food.refresh()
            snake.next_size()
            scoreboard.increase_score()


screen.exitonclick()

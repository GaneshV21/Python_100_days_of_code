from turtle import Turtle,Screen
from paddle import Paddle
from score import Score

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

paddle=Paddle()
score=Score()

screen.listen()
screen.onkey(paddle.up,"Up")
screen.onkey(paddle.down,"Down")
screen.onkey(paddle.W,"w")
screen.onkey(paddle.S,"s")


game_is_on = True
while game_is_on:
    screen.update()

    #ball move
    paddle.ball_move()

    #check who wins max -3 points
    if score.score1==3 or score.score2==3:
        game_is_on = False
        score.message()

    #left side ball goes means
    elif paddle.arr[2].xcor() > 400 :
        score.left_increase_score()
        paddle.arr[2].goto(0,0)

    #right side ball goes means
    elif paddle.arr[2].xcor() < -400:
        score.right_increase_score()
        paddle.arr[2].goto(0, 0)











screen.exitonclick()
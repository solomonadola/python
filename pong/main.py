import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from score_board import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.screensize(800,600)
screen.title("pong")
screen.tracer(0)
left_paddle = Paddle(-350,0)
right_paddle = Paddle(350,0)

ball= Ball()

score_board = ScoreBoard()

screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()

    # detect collision with the wall

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()
        ball.speed *= 0.99

    # detect collision with the paddle

    if ball.distance(right_paddle) < 51 and ball.xcor() == 340 or ball.distance(left_paddle) < 51 and ball.xcor() == -340:
        ball.bounce_x()
        ball.speed *= 0.99


    # detect right misses
    if ball.xcor() > 360 :
        ball.reset_position()
        score_board.left_score += 1
        score_board.update_score()
    # detect left misses
    if  ball.xcor() < -360:
        ball.reset_position()
        score_board.right_score += 1
        score_board.update_score()


screen.exitonclick()
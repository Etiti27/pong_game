from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoresheet import Score

screen = Screen()
screen.tracer(0)
right_paddle = Paddle(position=(350, 0))
left_paddle = Paddle(position=(-350, 0))
ball = Ball()
score = Score()

screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title('Pong')
screen.listen()
screen.onkey(right_paddle.move_padding_down, 'Down')
screen.onkey(right_paddle.move_padding_up, 'Up')

screen.onkey(left_paddle.move_padding_down, 's')
screen.onkey(left_paddle.move_padding_up, 'w')
is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # bounce on the top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        print(ball.ycor())
        ball.bounce_y()

    # bounce on the shield on both right and left hs
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()

    #     ball miss
    if ball.xcor() > 370:
        ball.reset_ball()
        score.scoreline_right()
    if ball.xcor() < -370:
        ball.reset_ball()
        score.scoreline_left()

screen.exitonclick()

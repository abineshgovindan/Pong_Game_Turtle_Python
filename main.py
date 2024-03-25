from turtle import Turtle, Screen

from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)



left_p = Paddle((-350, 0))
right_p = Paddle((350, 0))
l_s = Score()
ball = Ball()

screen.listen()

screen.onkey(left_p.go_up, "w")
screen.onkey(left_p.go_down , "s")

screen.onkey(right_p.go_up, "Up")
screen.onkey(right_p.go_down , "Down")

game = True


while game:
    screen.update()
    time.sleep(ball.move_speed)


    ball.move()
    print(ball.move_speed)

    ##colliosion
    if ball.ycor() > 280 or  ball.ycor() < - 280:
        ball.bounce_y()

    if ball.distance(right_p) < 50 and ball.xcor() > 320 or ball.distance(left_p) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380 :
        ball.center()
        l_s.l_point()


    if ball.xcor() < -380:
        ball.center()
        l_s.r_point()














screen.exitonclick()
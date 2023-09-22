from turtle import Turtle, Screen
import  random
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    r_color = (r, g, b)
    return r_color

tim = Turtle()
tim.shape("arrow")
tim.color((23,43,55))
tim.speed('fastest')

for i in range(50):
    tim.circle(50)
    tim.setheading(tim.heading() + 10)












screen = Screen()
screen.exitonclick()
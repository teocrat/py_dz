import time
import turtle

from turtle_circle import turtle_circle


class TrafficLight:
    __color = 'white'

    def running(self):
        turtle.ht()
        turtle.up()
        turtle.goto(-150, 280)
        turtle.down()
        turtle.begin_fill()
        turtle.forward(300)
        turtle.right(90)
        turtle.forward(470)
        turtle.right(90)
        turtle.forward(300)
        turtle.right(90)
        turtle.forward(470)
        turtle.end_fill()
        turtle.setposition(0, 0)
        turtle_circle(70, 190, 70)
        turtle_circle(70, 50, 70)
        turtle_circle(70, -90, 70)
        turtle_circle(70, 190, 70, 'red')
        time.sleep(7)
        turtle_circle(70, 190, 70)
        turtle_circle(70, 50, 70, "yellow")
        time.sleep(2)
        turtle_circle(70, 190, 70)
        turtle_circle(70, 50, 70)
        turtle_circle(70, -90, 70, "green")
        time.sleep(7)


a = TrafficLight()

a.running()

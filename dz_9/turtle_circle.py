import turtle


def turtle_circle(x, y, r, color='white'):
    turtle.ht()
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


if __name__ in '__main__':
    turtle_circle(0, 120, 70, 'red')
    turtle_circle(0, -20, 70, 'yellow')
    turtle_circle(0, -160, 70, 'green')


# turtle.getscreen().mainloop()
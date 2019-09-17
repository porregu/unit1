import turtle
def house():
    for x in range(6):
        turtle.fd(100)
        turtle.left(90)
    turtle.right(50)
    for x in range(2):
        turtle.fd(80)
        turtle.left(103)
def goto(x, y):  # this function makes mobe the pen to a coordenate without showing the line
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
turtle.fillcolor("black")
turtle.begin_fill()
house()
turtle.end_fill()
goto(250,250)
turtle.fillcolor("orange")
turtle.begin_fill()
house()
turtle.end_fill()
goto(-250,-250)
turtle.fillcolor("red")
turtle.begin_fill()
house()
turtle.end_fill()
turtle.exitonclick()

import turtle
def octagon():
    for x in range(8):
        turtle.fd(100)
        turtle.left(45)
turtle.fillcolor("purple")
turtle.begin_fill()
octagon()
turtle.end_fill()
def goto1():
    turtle.up()
    turtle.goto(250,70)
    turtle.down()
goto1()
turtle.fillcolor("pink")
turtle.begin_fill()
octagon()
turtle.end_fill()
def goto2():
    turtle.up()
    turtle.goto(-150,-90)
    turtle.down()
goto2()
turtle.fillcolor("blue")
turtle.begin_fill()
octagon()
turtle.endfill()

def goto3():
    turtle.up()
    turtle.goto(250, -90)
    turtle.down()
goto3()
octagon()
turtle.fillcolor("red")
turtle.begin_fill()
octagon()
turtle.end_fill()
turtle.exitonclick()

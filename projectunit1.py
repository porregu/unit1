# by Guillermo Porres
# september 17,2019
# this program makes 4 octagons that dosent touch and making some functions
import turtle
def octagon():
    for x in range(8):
        turtle.fd(100)
        turtle.left(45)
def goto(x,y):# this function makes mobe the pen to a coordenate without showing the line
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
turtle.fillcolor("purple")
turtle.begin_fill()
octagon()
turtle.end_fill()
goto(200,150)
turtle.fillcolor("pink")
turtle.begin_fill()
octagon()
turtle.end_fill()
goto(-200,150)
turtle.fillcolor("blue")
turtle.begin_fill()
octagon()
turtle.end_fill()
goto(-200,-150)
turtle.fillcolor("red")
turtle.begin_fill()
octagon()
turtle.end_fill()
turtle.exitonclick()
#Draw 3 Circles
import turtle

turtle.reset()
turtle.penup()
turtle.setpos(-50,50)
turtle.color('blue')
turtle.pendown()
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.penup()
turtle.setpos(50,-50)
turtle.color('green')
turtle.pendown()
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.penup()
turtle.setpos(0,0)
turtle.color('red')
turtle.pendown()
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

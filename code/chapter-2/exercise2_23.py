import turtle

radius = eval(input("Enter the radius: "))
turtle.penup()
turtle.back(radius)
turtle.pendown()
turtle.circle(radius)
turtle.circle(-radius)
turtle.penup()
turtle.forward(radius * 2)
turtle.pendown()
turtle.circle(radius)
turtle.circle(-radius)
turtle.done()

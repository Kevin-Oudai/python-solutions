import turtle

radius = eval(input("Enter the radius: "))
turtle.penup()
turtle.back(radius)
turtle.pendown()
turtle.circle(radius, steps=6)
turtle.circle(-radius, steps=6)
turtle.penup()
turtle.forward(radius * 2)
turtle.pendown()
turtle.circle(radius, steps=6)
turtle.circle(-radius, steps=6)
turtle.done()

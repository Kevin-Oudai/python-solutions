import turtle

x1, y1 = eval(input("Enter the center of rectangle (x1, y1): "))
width = eval(input("Enter the width: "))
height = eval(input("Enter the height: "))

turtle.penup()
turtle.goto(x1, y1)
turtle.forward(width / 2.0)
turtle.pendown()
turtle.right(90)
turtle.forward(height / 2.0)
turtle.right(90)
turtle.forward(width)
turtle.right(90)
turtle.forward(height)
turtle.right(90)
turtle.forward(width)
turtle.right(90)
turtle.forward(height / 2.0)
turtle.done()

import turtle

x1, y1 = eval(input("Enter the center of the circle: "))
radius = eval(input("Enter the radius: "))

area = 3.14 * radius ** 2

turtle.write(area)

turtle.penup()
turtle.goto(x1, y1 - (radius / 2.0))
turtle.pendown()
turtle.circle(radius)
turtle.done()

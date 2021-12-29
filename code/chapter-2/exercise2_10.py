speed, acceleration = eval(input("Enter speed and acceleration: "))
length = (speed ** 2) / (2 * acceleration)
print("The minimum runway length for this airplane is {:.3f}".format(length))

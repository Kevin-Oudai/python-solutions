temp = eval(input("Enter the temperature in Fahrenheit between -58 and 41: "))
speed = eval(input("Enter the wind speed in miles per hour: "))
chill = 35.74 + 0.6215 * temp - 35.75 * \
    speed ** 0.16 + 0.4275 * temp * speed ** 0.16
print("The wind chill index is {:.5f}".format(chill))

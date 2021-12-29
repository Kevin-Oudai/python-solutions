number = eval(input("Enter an integer: "))
print("{}".format(number // 1000))
number = number % 1000
print("{}".format(number // 100))
number = number % 100
print("{}".format(number // 10))
number = number % 10
print("{}".format(number))

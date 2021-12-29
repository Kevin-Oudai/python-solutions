digits = eval(input("Enter a number between 0 and 1000: "))
total = 0
total = total + digits % 10
digits = digits // 10
total = total + digits % 10
digits = digits // 10
total = total + digits % 10
digits = digits // 10
print("The sum of the digits is {}".format(total))

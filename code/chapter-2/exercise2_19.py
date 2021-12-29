investment = eval(input("Enter investment amount: "))
rate = eval(input("Enter annual interest rate: "))
years = eval(input("Enter number of years: "))

future = investment * (1 + (rate / 1200.0)) ** (years * 12)

print("Accumulated value is {:.2f}".format(future))

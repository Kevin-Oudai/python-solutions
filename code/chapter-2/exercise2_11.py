final_value = eval(input("Enter final account value: "))
interest = eval(input("Enter annual interest rate in percent: "))
monthlyInterest = interest / 1200.0
years = eval(input("Enter number of years: "))
numberOfMonths = years * 12
deposit = (1.0 * final_value) / ((1 + monthlyInterest) ** numberOfMonths)
print("Initial deposit value is {:.2f}".format(deposit))

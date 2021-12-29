balance, rate = eval(
    input("Enter balance and interest rate (e.g., 3 for 3%): "))

interest = balance * (rate / 1200.0)

print("The interest is {:.5f}".format(interest))

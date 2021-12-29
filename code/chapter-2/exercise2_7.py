minutes = eval(input("Enter a number between 0 and 1000: "))
hours = minutes // 60
days = hours // 24
years = days // 365
days = days % 365
print("{} minutes is approximately {} years and {} days".format(minutes, years, days))

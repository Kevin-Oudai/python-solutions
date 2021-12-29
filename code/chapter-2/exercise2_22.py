current_population = 312032486
years = eval(input("Enter the number of years: "))
days = 365
hours = days * 24
mins = hours * 60
secs = mins * 60
five_year = current_population + \
    (years * secs // 7) - (years * secs // 13) + (years * secs // 45)

print("The population in {} years is: {}".format(years, five_year))

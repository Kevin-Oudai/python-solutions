current_population = 312032486
days = 365
hours = days * 24
mins = hours * 60
secs = mins * 60
first_year = current_population + \
    (1 * secs // 7) - (1 * secs // 13) + (1 * secs // 45)
second_year = current_population + \
    (2 * secs // 7) - (2 * secs // 13) + (2 * secs // 45)
third_year = current_population + \
    (3 * secs // 7) - (3 * secs // 13) + (3 * secs // 45)
four_year = current_population + \
    (4 * secs // 7) - (4 * secs // 13) + (4 * secs // 45)
five_year = current_population + \
    (5 * secs // 7) - (5 * secs // 13) + (5 * secs // 45)

print("First Year: {}".format(first_year))
print("second Year: {}".format(second_year))
print("third Year: {}".format(third_year))
print("four Year: {}".format(four_year))
print("five Year: {}".format(five_year))

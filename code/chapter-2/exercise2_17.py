pounds = eval(input("Enter weight in pounds: "))
kilograms = pounds * 0.45359237
inches = eval(input("Enter height in inches: "))
meters = inches * 0.0254
bmi = kilograms / meters**2
print("BMI is {:.4f}".format(bmi))

subtotal, rate = eval(input("Enter the subtotal and a gratuity rate: "))
gratuity = rate * subtotal / 100.0
print("The gratuity is {:.2f} and the total is {:.2f}".format(
    gratuity, subtotal + gratuity))

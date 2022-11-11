"""
This program computes the area of a pentagon.
"""
import math
length = float(input("Enter the length from the center to a vertex: "))
s = math.sin(math.pi / 5) * 2 * length
area = (3 * math.sqrt(3) * s ** 2) / 2
print(f"The area of the pentagon is {area:.2f}")

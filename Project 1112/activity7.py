import math

def circumference(radius):
    result = 2 * math.pi * radius
    return result

radius = float(input("Enter the radius of the circle: "))

c = circumference(radius)
print(f"The circumference of the circle is: {c:.2f}")
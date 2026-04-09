import math

angle = float(input("Enter the angle in degrees: "))

radians = math.radians(angle)

sin_value = math.sin(radians)
cos_value = math.cos(radians)
tan_value = math.tan(radians)

print(f"\nAngle: {angle} degrees")
print(f"sin({angle}) = {sin_value:.4f}")
print(f"cos({angle}) = {cos_value:.4f}")
print(f"tan({angle}) = {tan_value:.4f}")
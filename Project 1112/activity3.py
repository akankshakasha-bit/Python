decimal = int(input("Enter a decimal number: "))

original = decimal

binary = ""
remainder = 0

while decimal > 0:
    remainder = decimal % 2      # Get remainder (0 or 1)
    binary = str(remainder) + binary  # Add to the LEFT of the string
    decimal = decimal // 2       # Divide by 2

print("Binary of", original, "is:", binary)
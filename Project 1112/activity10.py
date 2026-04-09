try:
    age = input("Enter your age: ")

    if "." in age:
        raise ValueError("Decimal values are not allowed!")

    age = int(age)

    if age <= 0:
        raise ValueError("Age cannot be zero or negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")

    print(f"\nAge entered: {age}")
    if age % 2 == 0:
        print(f"{age} is an Even number.")
    else:
        print(f"{age} is an Odd number.")

except ValueError as e:
    print(f"\nValue Error: {e}")
    print("Please enter a valid whole number for age!")
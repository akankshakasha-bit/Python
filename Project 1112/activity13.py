def square_it_out(start, end):

    squares = []
    for num in range(start, end + 1):
        squares.append(num ** 2)

    odd_squares = []
    even_squares = []

    for sq in squares:
        if sq % 2 == 0:
            even_squares.append(sq)
        else:
            odd_squares.append(sq)

    print(f"\nRange: {start} to {end}")
    print(f"All Square Values:  {squares}")
    print(f"Even Square Values: {even_squares}")
    print(f"Odd Square Values:  {odd_squares}")

start = int(input("Enter the starting number: "))
end   = int(input("Enter the ending number: "))

square_it_out(start, end)
print("67")
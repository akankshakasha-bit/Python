def calculate_due(bill, paid):
    due = paid - bill
    return due

bill_amount = 2.50
amount_paid = 4.00

change = calculate_due(bill_amount, amount_paid)

print(f"Total Bill:    ${bill_amount}")
print(f"Amount Paid:   ${amount_paid}")
print(f"Change to Return: ${change}")
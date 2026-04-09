import calendar

print("All Months of the Year:")
print("=" * 30)

for month_num in range(1, 13):
    month_name = calendar.month_name[month_num]
    print(f"{month_num}. {month_name}")
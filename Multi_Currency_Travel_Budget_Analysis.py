
# Multi-Currency Travel Budget Analysis

print("===== TRAVEL BUDGET ANALYSIS =====")

# Get travel budget in INR
budget = float(input("Enter your travel budget in INR: "))

# Number of expense categories
n = int(input("Enter number of expense categories: "))

categories = []
converted_expenses = []

total_expense = 0

# Enter expense details
for i in range(n):
    print("\nExpense", i + 1)

    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    currency = input("Enter currency code (USD/EUR/INR): ").upper()

    # Supplied exchange rates (sample values)
    if currency == "USD":
        rate = 84.0
    elif currency == "EUR":
        rate = 91.0
    elif currency == "INR":
        rate = 1.0
    else:
        print("Invalid currency! Expense skipped.")
        continue

    # Conversion fee of 2%
    converted_amount = amount * rate
    fee = converted_amount * 0.02

    final_amount = converted_amount + fee

    categories.append(category)
    converted_expenses.append(final_amount)

    total_expense = total_expense + final_amount

    print("Converted amount in INR:", round(converted_amount, 2))
    print("Conversion fee:", round(fee, 2))
    print("Final expense in INR:", round(final_amount, 2))


# Display expense details
print("\n===== EXPENSE SUMMARY =====")

for i in range(len(categories)):
    print(categories[i], ":", round(converted_expenses[i], 2), "INR")

print("\nTotal Travel Expense:", round(total_expense, 2), "INR")

# Compare expense with budget
if total_expense > budget:
    print("Budget Status: Budget Exceeded")
    print("Extra Amount:", round(total_expense - budget, 2), "INR")

elif total_expense < budget:
    print("Budget Status: Within Budget")
    print("Remaining Amount:", round(budget - total_expense, 2), "INR")

else:
    print("Budget Status: Exactly Within Budget")


# Find largest expense category
if len(converted_expenses) > 0:
    largest = converted_expenses[0]
    largest_category = categories[0]

    for i in range(1, len(converted_expenses)):
        if converted_expenses[i] > largest:
            largest = converted_expenses[i]
            largest_category = categories[i]

    print("Largest Expense Category:", largest_category)
    print("Largest Expense Amount:", round(largest, 2), "INR")
else:
    print("No valid expenses entered.")

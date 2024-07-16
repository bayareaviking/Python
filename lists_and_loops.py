
#expenses = [10.50, 8, 5, 15, 20, 5, 3]
#sum = 0
# for x in expenses:
#     sum += x
total = 0
expenses = []

# for i in range(7): 
#     expenses.append(float(input("Enter an expense: ")))

numExpenses = int(input("Enter the number of expenses: "))

for i in range(numExpenses):
    expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)
print(f"You spent ${total}")
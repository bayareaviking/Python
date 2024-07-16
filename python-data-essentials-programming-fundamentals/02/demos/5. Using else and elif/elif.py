balance = float(input("What is your bank account balance? "))

if balance < 0:
    print("You are in debt.")
elif balance < 2000:
    print("You are not in debt.")
    print("You cannot ask for a loan.")
else:
    print("You are not in debt.")
    print("You can ask for a loan.")
balance = float(input("What is your bank account balance? "))

if balance < 0:
    print("You are in debt.")

if balance >= 0:
    print("You are not in debt.")
    if balance < 2000:
        print("You cannot ask for a loan.")
    if balance >= 2000:
        print("You can ask for a loan.")
balance = float(input("What is your bank account balance? "))
age = int(input("What is your age? "))
have_job_input = input("Do you have a job? (yes/no) ")

if have_job_input == "y" or have_job_input == "yes":
    have_job = True
else:
    have_job = False

if age > 18 and age < 30:
    print("You can have some special benefits.")

if balance < 0:
    print("You are in debt.")
else:
    print("You are not in debt.")
    if balance < 2000 or age > 60 or age < 18 or not have_job:
        print("You cannot ask for a loan.")
    else:
        print("You can ask for a loan.")
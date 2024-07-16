print("Grocery list program")
grocery_list = []

while True:
    user_input = input("Input an item (type 'end' to finish): ")
    if user_input == "end":
        break
    grocery_list.append(user_input)

print("Here is your grocery list:")
for item in grocery_list:
	print(f"{item}")
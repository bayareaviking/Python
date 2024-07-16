def separate_section():
	print("-" * 80)


print("Grocery list program")
grocery_list = []

while True:
    user_input = input("Input an item (type 'end' to finish): ")
    if user_input == "end":
        break
    grocery_list.append(user_input)

separate_section()

print("Here is your grocery list:")
for item in grocery_list:
	print(f"{item}")

separate_section()

for item in grocery_list:
	if item == "bread":
		print("Bread is on the list!")
		break
else:
	print("Bread is not on the list.")
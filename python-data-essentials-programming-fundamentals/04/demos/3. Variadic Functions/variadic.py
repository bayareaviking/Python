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

def find_in_list(some_list, *item_names):
    for item_name in item_names:
        for item in some_list:
            if item == item_name:
                print(f"{item_name} is on the list!")
                break
        else:
            print(f"{item_name} is not on the list!")

find_in_list(grocery_list, "potatoes", "carrots", "bread")
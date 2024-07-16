print("Grocery list program")
grocery_list = []
user_input = None

while user_input != "end":
    user_input = input("Input an item (type 'end' to finish): ")
    if user_input != "end":
        grocery_list.append(user_input)

print("Here is your grocery list:")
i = 0
while i < len(grocery_list):
    print(f"{grocery_list[i]}")
    i = i + 1
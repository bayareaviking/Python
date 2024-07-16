def separate_section():
	print("-" * 80)


print("Grocery list program")
grocery_list = {}

while True:
    item_name_input = input("Input an item (type 'end' to finish): ")
    if item_name_input == "end":
        break
    item_price_input = input("Input an item's price: ")
    grocery_list[item_name_input] = float(item_price_input)

separate_section()

print("Here is your grocery list:")
for name, price in grocery_list.items():
	print(f"{name}: {price}")

separate_section()

def find_in_dict(some_dict, *item_names):
    for item_name in item_names:
        for item in some_dict.keys():
            if item == item_name:
                print(f"{item_name} is on the list!")
                break
        else:
            print(f"{item_name} is not on the list.")

def groceries_total_cost(grocery_list):
    total_cost = 0
    for item_price in grocery_list.values():
	      total_cost += item_price
    return total_cost

find_in_dict(grocery_list, "potatoes", "carrots", "bread")
separate_section()
price = groceries_total_cost(grocery_list)
print("Total amount:", price)
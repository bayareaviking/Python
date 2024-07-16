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

for item in grocery_list:
    if item == "bread":
        print("Bread is on the list!")
        break
else:
    print("Bread is not on the list.")

# bread_on_list = False
# for item in grocery_list:
#     if item == "bread":
#         print("Bread is on the list!")
#         bread_on_list = True
#         break

# if not bread_on_list:
#     print("Bread is not on the list.")
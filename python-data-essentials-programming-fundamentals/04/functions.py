# Quick refresher on functions

def separate_section():
	print("-" * 80 + "\n")
    

print("Grocery list program")


def return_funct(value):
	if value >= 10:
		var = True
	else:
		var = False
	return var;


receivedValue = input("Please enter an integer: ")

print(return_funct(int(receivedValue)))
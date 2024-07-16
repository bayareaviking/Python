# Quick refresher on dictionaries

# Brackets when creating a "list-style" dictionary
supply = {'apple': 4, 'mango': 6, 'orange': 8}

print(supply)

# Modifying the dictionary with square brackets
supply['mango'] = 5
print(supply['mango'])

# Using the dict() function to create a dictionary, remember that they're params
basket = dict(orange = 1.2)
print(basket)
print(type(basket))

# If an element does not exist in the existing dictionary, it will be added
# Easiest way to add or modify element
basket['lemon'] = 0.9
supply['kiwi'] = 12

print(basket)

print(sorted(supply.keys()))

print(supply.get('kiwi'))
print(supply.get('starfruit', 'This fruit is not in the inventory'))

# Another way to add or modify a key-value pair to a dictionary
supply.update({'cucumber': 69})

print(supply)

del supply['cucumber']

print(supply)

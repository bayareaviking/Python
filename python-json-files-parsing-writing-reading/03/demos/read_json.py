import json

with open('03/demos/coffee_sales/coffee_sales_1.json', 'r') as f:
    data = json.load(f)

for item in data:
    print(item)
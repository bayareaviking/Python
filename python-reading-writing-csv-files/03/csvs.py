import csv
import requests
import codecs

r = requests.get('https://api.github.com')
r.status_code
r.text

url = 'https://data.openei.org/files/5650/iou_zipcodes_2020.csv'
response = requests.get(url)
print(response)

text = response.iter_lines()
print(text)

cr = csv.reader(codecs.iterdecode(text, 'utf-8'), delimiter=',')
for i, row in enumerate(cr):
    if i == 0:
        print(f"Columns: {',' .join(row)}")
    elif i>2: 
        break
    print(row)
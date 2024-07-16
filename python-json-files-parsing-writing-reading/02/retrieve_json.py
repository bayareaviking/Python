import requests
import json

url = 'https://jsonplaceholder.typicode.com/users'
#url = 'https://jsonplaceholder.typicode.com/todos'

headers = {
    'Content-Type': 'application/json'
}

parameters = {
    #'location': 'London',
    #'start_date': '2021-03-01',
    #'end_date': '2021-03-1'
    #'userId': 10,
    'name': 'Clementina DuBuque',
}

res = requests.get(url, headers = headers, params = parameters)

if res.status_code == 200:
    data = json.loads(res.text)
    for item in data:
        print(item)
else:
    print('Error retrieving data with status code: ', res.status_code)
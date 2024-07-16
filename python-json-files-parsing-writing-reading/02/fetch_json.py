import json
import requests

url = 'https://edfreitas.me/test/wired_brain.json'

res = requests.get(url)

if res.status_code == 200:
    data = json.loads(res.text)
    for item in data:
        print(item)
else: 
    print('Error fetching data with status code: ', res.status_code)


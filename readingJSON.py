
import requests
uri = 'http://api.open-notify.org/astros.json'

response = requests.get(uri)
json = response.json()

print("\nPeople currently in space are: ")
for person in json['people']:
    print(f"{person['name']} is currently stationed on the {person['craft']}")
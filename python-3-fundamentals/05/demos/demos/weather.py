import requests

""" def get_weather_json(city):
    url = 'http://api.weatherapi.com/v1/current.json?key=d73af82268fa4a64a3c200007231402&q='+city+'&aqi=no'
    response = requests.get(url)
    weather_json = response.json()
    return weather_json """

def get_weather_json(city):
    url = 'http://api.weatherapi.com/v1/current.json?key=d73af82268fa4a64a3c200007231402&q='+city+'&aqi=no'
    return requests.get(url).json()

def get_current_temperature_f(json):
    temp = json.get('current').get('temp_f')
    return temp

def get_current_temperature_c(json):
    temp = json.get('current').get('temp_c')
    return temp

def get_current_description(json):
    desc = json.get('current').get('condition').get('text')
    return desc

def main():
    city = 'Los Angeles'
    weather_json = get_weather_json(city)
    temp_f = get_current_temperature_f(weather_json)
    temp_c = get_current_temperature_c(weather_json)
    description = get_current_description(weather_json)

    print(f"Today's weather in {city} is {description} and {temp_f}F / {temp_c}C")

main()
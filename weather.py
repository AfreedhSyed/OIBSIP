import requests

def get_weather(city):
    api_key = '37cfa2d88c9261f99873105bffb0c9c4'
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        print(f'Temperature: {temperature}°C')
        print(f'Humidity: {humidity}%')
        print(f'Conditions: {description}')
    else:
        print('Unable to fetch weather data.')

if __name__ == '__main__':
    city = input('Enter a city: ')
    get_weather(city)
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

def get_weather():
    city = input('Введите название города: ')
    api_key = '7d58c54b3c0c66b13dcff13b9c5134e7'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    x = response.json()
    if x['cod'] == 200:
        y = x['main']
        current_temperature = y['temp']
        current_pressure = y['pressure']
        current_humidity = y['humidity']
        print('Температура = ' + str(current_temperature))
        print('Атмосферное давление = ' + str(current_pressure))
        print('Влажность воздуха = ' + str(current_humidity))
    else:
        print(f'Информации о погоде в городе {city} не найдено!')

def get_joke():
    num = int(input('Введите рандомный номер шутки: '))
    response = requests.get('https://geek-jokes.sameerkumar.website/api?format=json')
    x = response.json()
    y = x['joke']
    print(y)

while True:
    admin = int(input('Введите действие которое хотите выбрать? 1-погода, 2-шутка: '))
    if admin == 1:
        get_weather()
    elif admin == 2:
        get_joke()
    else:
        print('Запрос непонятен. Попробуйте заново')


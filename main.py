import requests


url_template = 'https://wttr.in/{}?mnTq&lang=ru'
cities = ['Череповец', 'Лондон', 'Шереметьево']

for city in cities:
    url = url_template.format(city)
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)

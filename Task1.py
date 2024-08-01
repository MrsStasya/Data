# Урок 1. Основы клиент-серверного взаимодействия. Парсинг API
# 1. Ознакомиться с некоторые интересными API. https://docs.ozon.ru/api/seller/ https://developers.google.com/youtube/v3/getting-started https://spoonacular.com/food-api
# 2. Потренируйтесь делать запросы к API. Выберите публичный API, который вас интересует, и потренируйтесь делать API-запросы с помощью Postman. Поэкспериментируйте с различными типами запросов и попробуйте получить различные типы данных.
# 3. Сценарий Foursquare
# Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию (например, кофейни, музеи, парки и т.д.).
# Используйте API Foursquare для поиска заведений в указанной категории.
# Получите название заведения, его адрес и рейтинг для каждого из них.
# Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.

import requests
import json

# Ваши учетные данные API
client_id = "__"
client_secret = "__"

# Конечная точка API
endpoint = "https://api.foursquare.com/v3/places/search"

# Определение параметров для запроса API
city = input("Введите название города: ")
category = input("Введите категорию заведения: ")

params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "near": city,
    "query": category,
    "fields":"name,location,rating"
}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3V3AFHzvqod5PVkb9j5ptfec29VfLTGG2XbHrQEGC8bI="
}

# Отправка запроса API и получение ответа
response = requests.get(endpoint, params=params,headers=headers) #endpoint = url

# Проверка успешности запроса API
if response.status_code == 200:
    print("Успешный запрос API!")
    data = json.loads(response.text)#парсим в json файл ответ
    venues = data["results"]#получаем список мест из ответа
    for venue in venues: #проходимся по каждому месту в списке
        print("Название:", venue["name"])
        try:
            print("Адрес:", venue["location"]["address"])
        except Exception:
            print("Адрес не найден")
        try:
            print("Рейтинг:", venue["rating"])
        except Exception:
            print("Рейтинг отсутствует")
        print("\n")
else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)

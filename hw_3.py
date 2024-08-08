# 1.	Установите MongoDB на локальной машине, а также зарегистрируйтесь в онлайн-сервисе.
#  https://www.mongodb.com/ https://www.mongodb.com/products/compass
# 2.	Загрузите данные который вы получили на предыдущем уроке путем скрейпинга сайта с помощью Buautiful Soup в MongoDB
# и создайте базу данных и коллекции для их хранения.
# 3.	Поэкспериментируйте с различными методами запросов.
# 4.	Зарегистрируйтесь в ClickHouse.
# 5.	Загрузите данные в ClickHouse и создайте таблицу для их хранения.

from clickhouse_driver import Client
from pymongo import MongoClient
import json

# Подключение к MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Создание базы данных
database_name = "homework_3"
database = client[database_name]

# Создание коллекции и загрузка данных из файла JSON
collection_name = "books_toscrape"
collection = database[collection_name]

# Чтение данных из файла JSON
with open("books_data.json", encoding='utf-8') as file:
    data = json.load(file)

# Вставка данных в коллекцию
collection.insert_many(data)

# Закрытие соединения с MongoDB
client.close()

# # Подключение к серверу ClickHouse передэтим установка pip install clickhouse-driver
# client = Client('localhost')



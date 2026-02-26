import requests

# Список сайтов
urls = [
    "https://github.com/",
    "https://www.binance.com/en",
    "https://tomtit.tomsk.ru/",
    "https://jsonplaceholder.typicode.com/",
    "https://moodle.tomtit-tomsk.ru/"
]

# Проверяем каждый сайт
for url in urls:
    try:
        response = requests.get(url)  # делаем GET-запрос
        print(f"URL: {url}")  # показываем адрес
        print(f"Код ответа: {response.status_code}")  # показываем код ответа

        # Определяем статус по коду
        if response.status_code == 200:
            print("Статус: доступен")
        elif response.status_code == 404:
            print("Статус: не найден")
        elif response.status_code == 403:
            print("Статус: вход запрещен")
        else:
            print("Статус: недоступен")

        print()  # пустая строка для разделения сайтов

    except requests.exceptions.RequestException as e:
        # Если сайт недоступен
        print(f"URL: {url}")
        print(f"Статус: недоступен")
        print(f"Ошибка: {e}")
        print()

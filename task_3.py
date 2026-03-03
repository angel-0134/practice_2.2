import requests
import json

url = "https://www.cbr-xml-daily.ru/daily_json.js"
response = requests.get(url)
data = response.json()

valutes = data["Valute"]

groups = {}

while True:
    print("\n1 - Показать все валюты")
    print("2 - Найти валюту по коду")
    print("3 - Создать группу")
    print("4 - Показать группы")
    print("0 - Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        for code, currency in valutes.items():
            print(f"{code} - {currency['Name']} - {currency['Value']}")

    elif choice == "2":
        code = input("Введите код валюты: ").upper()
        if code in valutes:
            currency = valutes[code]
            print(f"{currency['Name']} - {currency['Value']}")
        else:
            print("Валюта не найдена")

    elif choice == "3":
        group_name = input("Введите название группы: ")
        groups[group_name] = []

        print("Добавляйте валюты. Просто нажмите Enter чтобы закончить.")

        while True:
            currency_code = input("Код валюты: ").upper()
            if currency_code == "":
                break
            if currency_code in valutes:
                groups[group_name].append(currency_code)
                print("Добавлено")
            else:
                print("Валюта не найдена")

        # Сохраняем сразу после создания
        with open("save.json", "w", encoding="utf-8") as f:
            json.dump(groups, f, ensure_ascii=False, indent=4)

        print("Группа сохранена!")

    elif choice == "4":
        print(groups)

    elif choice == "0":
        break

    else:
        print("Неверный выбор")

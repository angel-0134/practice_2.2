import requests

url = "https://www.cbr-xml-daily.ru/daily_json.js"
response = requests.get(url)
data = response.json()
data["Valute"]
for code, currency in data["Valute"].items():
    print(f"{code} - {currency['Name']} - {currency['Value']}")

    code = input("Введите код валюты: ").upper()

    if code in data["Valute"]:
        currency = data["Valute"][code]
        print(currency["Name"], currency["Value"])
    else:
        print("Валюта не найдена")
        groups = {
            "Моя группа": ["USD", "EUR"]
        }
        import json

        with open("save.json", "w", encoding="utf-8") as f:
            json.dump(groups, f, ensure_ascii=False, indent=4)

            with open("save.json", "r", encoding="utf-8") as f:
                groups = json.load(f)

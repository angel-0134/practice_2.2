# код не работает, это какое мошенничество (поэтому удалила 1 строчку) 
import requests

def get_profile():
    username = input("Введите имя пользователя GitHub: ")
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("\nПрофиль пользователя")
        print("Имя:", data.get("name"))
        print("Ссылка:", data.get("html_url"))
        print("Количество репозиториев:", data.get("public_repos"))
        print("Количество подписчиков:", data.get("followers"))
        print("Количество подписок:", data.get("following"))
        print()
    else:
        print("Пользователь не найден.\n")


def get_repositories():
    username = input("Введите имя пользователя GitHub: ")
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()
        print(f"\nРепозитории пользователя {username}\n")

        if not repos:
            print("У пользователя нет репозиториев.\n")
            return

        for repo in repos:
            print("Название:", repo.get("name"))
            print("Ссылка:", repo.get("html_url"))
            print("Язык:", repo.get("language"))
            print("Видимость:", repo.get("visibility"))
            print("Ветка по умолчанию:", repo.get("default_branch"))
            print("-" * 40)
        print()
    else:
        print("Ошибка получения репозиториев.\n")


def search_repositories():
    query = input("Введите название репозитория для поиска: ")
    url = f"https://api.github.com/search/repositories?q={query}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        items = data.get("items", [])

        print("\nРезультаты поиска\n")

        if not items:
            print("Ничего не найдено.\n")
            return

        for repo in items[:5]:  # показываем первые 5
            print("Название:", repo.get("name"))
            print("Ссылка:", repo.get("html_url"))
            print("Язык:", repo.get("language"))
            print("-" * 40)
        print()
    else:
        print("Ошибка поиска.\n")

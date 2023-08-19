import requests
from bs4 import BeautifulSoup

# Запросить содержимое страницы
url = "https://m.avito.ru/ekaterinburg/doma_dachi_kottedzhi/sdam/na_dlitelnyy_srok-ASgBAgICAkSUA9IQoAjIVQ?context=H4sIAAAAAAAAA0u0MrKqLraysFJKK8rPDUhMT1WyhnBTE0tKi1JTQFxDAyulksSi9NQSmAJzQyulC7Mu7Luw52LLhX0XGy42Xdh7sfvCVoULW0CCFzYoXNh0aMGFDRcbLmy9sPfClovNOgoX5gOldl3YcGE7ULzpYg9QycXGC1uVrGsBxCDoyoUAAAA&f=ASgBAQICAkSUA9IQoAjIVQJAkL0ORPak0QH0pNEB8qTRAfCk0QGUvQ4U~KTRAQ&radius=0&s=104&presentationType=serp"
response = requests.get(url)
content = response.text

# Создать объект BeautifulSoup
soup = BeautifulSoup(content, "html.parser")

# Найти заголовки новостей
titles = soup.find_all("p", class_="V6MvH KSyZc")

# Вывести заголовки новостей
for title in titles:
    print(title.get_text(strip=True))
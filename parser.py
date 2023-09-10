import requests
from bs4 import BeautifulSoup
c = 0
# Запросить содержимое страницы
url = 'https://www.avito.ru/ekaterinburg/tovary_dlya_kompyutera/dzhoystiki_i_ruli-ASgBAgICAUTGB7ZO?cd=1&q=%D0%B3%D0%B5%D0%B9%D0%BC%D0%BF%D0%B0%D0%B4'
requests = requests.get(url)
bs = BeautifulSoup(requests.text, 'html.parser')

all_links = bs.find_all('a', class_='iva-item-sliderLink-uLz1v')

for link in all_links:
    print("avito.ru"+link["href"])


from bs4 import BeautifulSoup
import requests
import random

import sqlite3


db = sqlite3.connect("Triangle_Kino.db")
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Triangle_Kino (
    ID INTEGER PRIMARY KEY,
    RESURS TEXT,
    NAME TEXT,
    GOD TEXT,
    OPISANIE TEXT,
    LINK_STR TEXT
)""")
db.commit()

resursZERO = "SITE_Name"

user_agent_list = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]

user_agent = random.choice(user_agent_list)
headers = {'User-Agent': user_agent}

x = 1

url = "https://lordfilm.do/"


while True:
    i = 0
    page = BeautifulSoup(requests.get(url,headers=headers).text, "lxml")


    name_list = []
    god_list = []
    link1_list = []
    opisanie_list = []


    for name in page.find_all("div", class_="th-title"):
        name_text = name.text
        print(name_text)
        name_list.append(name_text)

    for god in page.find_all("div", class_="th-year"):
        god_text = god.text
        print(god_text)
        god_list.append(god_text)

    for film in page.find_all("div", class_="th-item"):
        Link_STR = film.find("a", class_="th-in with-mask").get('href')
        print(Link_STR)
        link1_list.append(Link_STR)


    for link0 in link1_list:

        page2 = BeautifulSoup(requests.get(link0,headers=headers).text, "lxml")

        opisanie = page2.find("div", class_="fdesc clearfix slice-this").text

        print(len(god_list))

        b_split_list = opisanie.split("                     ")
        b1 = b_split_list[-1]
        print(b1)


        opisanie_list.append(b1)


    while i < len(opisanie_list):
        name1 = name_list[i]
        god1 = god_list[i]
        opisanie1 = opisanie_list[i]
        link2 = link1_list[i]

        cur.execute("""INSERT INTO Triangle_Kino (RESURS, NAME, GOD, OPISANIE, LINK_STR) VALUES (?, ?, ?, ?, ?);""", (resursZERO, name1, god1, opisanie1, link2))
        db.commit()
        print("Добавлено " + str(i))
        i = i + 1


    x = x + 1

    url = "https://lordfilm.do/" + str(x) + "/"


    if x == 1783:
        break
    


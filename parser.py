import requests
from bs4 import BeautifulSoup
import pprint

domain = 'https://pythonworld.ru'
url = f'{domain}/bookshop'

response = requests.get(url)


# print(response.status_code)

# print(response.text)

# Создаем суп для разбора html
soup = BeautifulSoup(response.text, 'html.parser')

result = {}
booknames_a = soup.find_all('div', class_='bookname')
for one_booknames_a in booknames_a[:1]:
    text = one_booknames_a.text

    # print(text, title)
    text1 = text.replace('\n','')
bookauthors_a = soup.find_all('div', class_='bookauthor')
titles = []
for bookauthor_a in bookauthors_a[:1]:
    print(bookauthor_a.text)
titles.append(bookauthor_a.text)
#
#     # добавим в словарь
result[text1] = titles
#
pprint.pprint(result)
# Поиск по классу - Обычно самое полезное!!!

# big_body_div = soup.find('div', class_='modulebody1')

# print(big_body_div)
# print(type(big_body_div))
# print(big_body_div.get('class'))

# 1. Лучший вариант искать тожде по классу
# Можно искать в уже найденном
# modulebody3 = big_body_div.find('div', class_='modulebody3')
# print(modulebody3)

# 2. Если не получается найти по классу или по тегу, то придется по порядку
# .contents

# print(big_body_div.contents)
# print(len(big_body_div.contents))
# находим ссылку a по порядку
# print(big_body_div.contents[1].contents[1].contents)

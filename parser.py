import requests
from bs4 import BeautifulSoup
import pprint
import json

domain = 'https://pythonworld.ru'
url = f'{domain}/bookshop'

response = requests.get(url)

# print(response.status_code)

# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

names = []
booknames_a = soup.find_all('div', class_='bookname')
for one_booknames_a in booknames_a[:5]:
    text = one_booknames_a.text
    text1 = text.replace('\n','')
    names.append(text1.strip())

bookauthors_a = soup.find_all('div', class_='bookauthor')
titles = []
for bookauthor_a in bookauthors_a[:5]:
    print(bookauthor_a.text)
    titles.append(bookauthor_a.text)

    # добавим в словарь
result = dict(zip(names,titles))

pprint.pprint(result)

with open("result.json", "w", encoding='utf-8') as parser_file:
    json.dump(result, parser_file)
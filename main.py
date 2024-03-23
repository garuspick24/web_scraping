import requests
from bs4 import BeautifulSoup

url = 'https://www.visidarbi.lv/darba-sludinajumi?page=1#results'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

# # Приклад: знаходження всіх елементів з тегом <a>
links = soup.find_all('a', class_='long-title')
for link in links:
    if link:
        title = link.text
        print(title)


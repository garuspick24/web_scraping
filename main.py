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

city = soup.find_all('li', class_='location')
for i in city:
    if i:
        title = i.text
        print(title.strip())

pirms = soup.find_all('li', class_='added')
for i in pirms:
    if i:
        title = i.text
        print(title.strip())

salary = soup.find_all('li', class_="salary")
for i in salary:
    if i:
        title = i.text
        print(title.strip())

company = soup.find_all('li', class_="company")
for i in company:
    if i:
        title = i.text
        print(title.strip())

day_date = soup.find_all('li', class_="duedate")
for i in day_date:
    if i:
        title = i.text
        print(title.strip())






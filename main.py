import sqlite3
import requests
from bs4 import BeautifulSoup


conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS job_ads (
        id INTEGER PRIMARY KEY,
        title TEXT,
        city TEXT,
        time TEXT,
        salary TEXT,
        company TEXT,
        due_date TEXT
    )
''')
conn.commit()



# Закриття підключення
conn.close()



url = 'https://www.visidarbi.lv/darba-sludinajumi?page=1#results'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

# parsing data from each advertisement on one page
counter = 0
for title_index in range(len(soup.select(".title"))):
    all_information = []
    if soup.select(".title")[title_index].select("a"):
        title_ads = (soup.select(".title")[title_index].select("a")[0].text.strip())
        all_information.append(title_ads)

        counter += 1

        soup.select(".title")[title_index].select("a")[0].get('href')
        if soup.select(".details")[title_index].select("li"):
            for index in range(5):
                details = soup.select(".details")[title_index].select("li")[index].text.strip()
                print(soup.select(".details")[title_index].select("li")[index].text.strip())
                all_information.append(details)
    title, city, time_, salary, company, due_date = all_information

    job_ad = (title, city, time_, salary, company, due_date)

    cursor.execute('INSERT INTO job_ads (title, link) VALUES (?, ?)', job_ad)
    conn.commit()
    print("---------------------------------------------------")


print(counter)

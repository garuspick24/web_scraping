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

page = 1

while True:
    url = f'https://www.visidarbi.lv/darba-sludinajumi?page={page}#results'
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    if len(soup.select(".title")):

        counter = 0
        for title_index in range(len(soup.select(".title"))):
            all_information = [None, None, None, None, None, None]

            if soup.select(".title")[title_index].select("a"):
                counter += 1
                title_ads = (soup.select(".title")[title_index].select("a")[0].text.strip())
                all_information[0] = title_ads
                soup.select(".title")[title_index].select("a")[0].get('href')
                # print(title_ads)

                if soup.select(".details")[title_index].select("li"):
                    for index in range(5):
                        try:
                            details = soup.select(".details")[title_index].select("li")[index].text.strip()
                            if details:
                                # print(soup.select(".details")[title_index].select("li")[index].text.strip())
                                all_information[index + 1] = details
                        except Exception as e:
                            print(f"Error: {e}")

                title, city, time_, salary, company, due_date = all_information

                job_ad = (title, city, time_, salary, company, due_date)
                cursor.execute(
                    'INSERT INTO job_ads (title, city, time, salary, company, due_date) VALUES (?, ?, ?, ?, ?, ?)',
                    job_ad)
                conn.commit()


                # print("---------------------------------------------------")

        page += 1
    else:
        break

# Закриття підключення
conn.close()

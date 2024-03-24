import requests
from bs4 import BeautifulSoup

url = 'https://www.visidarbi.lv/darba-sludinajumi?page=1#results'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

# parsing data from each advertisement on one page
counter = 0
for title_index in range(len(soup.select(".title"))):

    if soup.select(".title")[title_index].select("a"):
        print(soup.select(".title")[title_index].select("a")[0].text.strip())

        counter += 1

        soup.select(".title")[title_index].select("a")[0].get('href')
        if soup.select(".details")[title_index].select("li"):
            for index in range(5):
                print(soup.select(".details")[title_index].select("li")[index].text.strip())
    print("---------------------------------------------------")


print(counter)

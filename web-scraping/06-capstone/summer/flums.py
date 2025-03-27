from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

base_url = "https://www.flumserberg.ch/de/informationen/Geoeffnete-Anlagen"
html_page = urlopen(base_url + "/Winter")
html_text = html_page.read().decode("utf-8")

soup = BeautifulSoup(html_text, "html.parser")
restaurant_container = soup.find("div", {"id": "facilities-restaurant"})

# Get the table
table_restaurants = restaurant_container.find('table', class_="table facility-table")

header = []
rows = []
for i, row in enumerate(table_restaurants.find_all('tr')):
    if i == 0:
        header = [el.text.strip() for el in row.find_all('th')]
    else:
        data = row.find('span')
        # print(data)
        # print(type(data))

        ### Exercise ####
        title = # use get to get title
        icon = # use get to get icons (see class)

        status = "open"
        # set status to closed if icon-close appears

        rows.append([title, status])

print(rows)

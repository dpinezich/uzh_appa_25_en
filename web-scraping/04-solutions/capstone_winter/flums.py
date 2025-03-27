from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

base_url = "https://www.flumserberg.ch/de/informationen/Geoeffnete-Anlagen"
html_page = urlopen(base_url + "/Winter")
html_text = html_page.read().decode("utf-8")

soup = BeautifulSoup(html_text, "html.parser")
live_items = soup.find_all("li", class_="live-infos__item")

slopes = live_items[0]
temperature = live_items[2]


# print(slopes)
# print(temperature)

def clean_and_print_data(soup_element):
    print(soup_element.find("span", class_="live-infos__item-text").get_text().strip())


clean_and_print_data(slopes)
clean_and_print_data(temperature)

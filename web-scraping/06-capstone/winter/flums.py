from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


base_url = "https://www.flumserberg.ch/de/informationen/Geoeffnete-Anlagen"
html_page = urlopen(base_url + "/Winter")
html_text = html_page.read().decode("utf-8")

soup = BeautifulSoup(html_text, "html.parser")
live_items = soup.find_all("li", class_="live-infos__item")

print(live_items)
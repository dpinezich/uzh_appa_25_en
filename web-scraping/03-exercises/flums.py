from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

base_url = "https://www.flumserberg.ch/de/informationen/Geoeffnete-Anlagen"
html_page = urlopen(base_url + "/Winter")
html_text = html_page.read().decode("utf-8")

soup = BeautifulSoup(html_text, "html.parser")
# todo add the correct class
live_items = soup.find_all("li", class_="....????")

# todo get slopes and temperature
#slopes =
#temperature =

#print(slopes)
#print(temperature)

#def clean_and_print_data(soup_element):
    # todo write a function that cleans and strips

# todo uncomment when ready
#clean_and_print_data(slopes)
#clean_and_print_data(temperature)
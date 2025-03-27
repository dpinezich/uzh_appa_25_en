from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.digitec.ch/de/s1/product/hp-probook-455-g10-1560-amd-ryzen-7-7730u-16-gb-512-gb-ch-notebook-36992532"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# first level
# <button class="sc-7a96f06e-5 ijhpDf"><span aria-label="2199 CHF">2199.–</span></button>
price = soup.find("button", class_="sc-7a96f06e-5 ijhpDf")

html_array = []
for d in price.descendants:
    html_array.append(d)

print(html_array[1])

title = soup.find("h1", class_="sc-881b1c9a-0 gcjDEs")
print(title.get_text())
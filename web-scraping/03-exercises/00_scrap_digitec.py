from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.digitec.ch/de/s1/product/sony-alpha-7-iv-33-mpx-vollformat-kamera-17071964"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# first level
# <button class="sc-7a96f06e-5 ijhpDf"><span aria-label="2199 CHF">2199.–</span></button>
price = soup.find("button", class_="sc-7a96f06e-5 ijhpDf")
print(price)

# second, third level
# <span aria-label="2199 CHF">2199.–</span>
# 2199.–
for d in price.descendants:
    print(d)
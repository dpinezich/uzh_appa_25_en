from urllib.request import urlopen
from bs4 import BeautifulSoup

base_url = "http://olympus.realpython.org"
html_page = urlopen(base_url + "/profiles")
html_text = html_page.read().decode("utf-8")

soup = BeautifulSoup(html_text, "html.parser")

print(soup)

# should print out:
# http://olympus.realpython.org/profiles/aphrodite
# http://olympus.realpython.org/profiles/poseidon
# http://olympus.realpython.org/profiles/dionysus
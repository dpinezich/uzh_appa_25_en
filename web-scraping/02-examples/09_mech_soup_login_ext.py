# 09_mech_soup_login_ext.py
import mechanicalsoup

# 1
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

# 2
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# 3
profiles_page = browser.submit(form, login_page.url)

# 4
print(profiles_page.url)

# 5
links = profiles_page.soup.select("a")
for link in links:
    address = link["href"]
    text = link.text
    print(f"{text}: {address}")

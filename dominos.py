from bs4 import BeautifulSoup
import requests
page = requests.get("https://dominos.by/")
soup = BeautifulSoup(page.text, features="html.parser")
data = soup.findAll("div", {"class": "product-card__title"})
for pizza in data:
    print(pizza.find(text=True, recursive=False).strip())
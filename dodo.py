import json
import requests
page = requests.get("https://dodopizza.by/api/menu?localityId=00000001-0000-0000-0000-000000000000")
data = json.loads(page.text)
for pizza in data["pizzas"]:
    print(pizza["name"])
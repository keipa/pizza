import json
import requests
page = requests.get("https://pzz.by/api/v1/pizzas?load=ingredients,filters&filter=meal_only:0&order=position:asc")
data = json.loads(page.text)
for pizza in data["response"]["data"]:
    print(pizza["title"])
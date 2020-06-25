import requests
import json

api = "~~~~~~"

apikey = "~~~~~~~"


cities = ["Seoul,KR", "Tokyo,JP", "New York,US"]

k2c = lambda k: k-273.15

for name in cities:
    url = api.format(city = name, key = apikey)
    res = requests.get(url)
    data = json.loads(res.text):wq

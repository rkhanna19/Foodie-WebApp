import requests
import pprint
url = "http://127.0.0.1:5000"
r = requests.get(url)
print(r)
data = r.json()
pprint(data)

# importing the requests library
import requests

payload = {'schluessel1': 'wert1', 'schluessel2': 'wert2'}
r = requests.get("https://httpbin.org/get", params=payload)

print(r.text)

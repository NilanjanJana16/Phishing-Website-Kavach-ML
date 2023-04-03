import requests

url = 'http://127.0.0.1:5000/api'
r = requests.post(url,json={'url': 'https://www.google.com'})

print(r.json())
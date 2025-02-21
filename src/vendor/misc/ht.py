import requests
cl = requests.get('https://google.de')
print(cl.text)
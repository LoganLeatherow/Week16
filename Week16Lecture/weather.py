import requests


api_key = ''
city = 'Orlando'
url = ""

request = requests.get(url)
json = request.json()
print(json)
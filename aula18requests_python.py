# requests para requisições HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
import requests

# http:// -> 80
# https:// -> 443
url = 'https://nerdfilmes.com.br/'
response = requests.get(url)

print(response.status_code)
print()
print(response.headers)
print()
print(response.content)
print()
print(response.text)
print()
# print(response.json())
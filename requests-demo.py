import requests

r = requests.get('https://relationalagents.com')

print(r.status_code)
print(r.text)
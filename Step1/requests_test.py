import requests
res = requests.get('https://example.com')
print(res.status_code)
print(res.text)

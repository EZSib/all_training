import requests

response = requests.get('https://example.com')
response1 = requests.get('https://example.com', params={'name': 'Bearer'})
'''Здесь мы передаем в качестве аргумента заголовок в виде словаря Python.'''
#response2 = requests.get('https://example.com, headers={'example-header': 'Bearer'})
url = 'https://example.com'
headers = {'Authorization': 'Bearer example-auth-code'}
payload = {'name':'Mark', 'email': 'mark@bearer.sh'}
response3 = requests.post(url, headers=headers, data=payload)

print(response3.text)

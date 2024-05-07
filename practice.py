import requests

api_key = 'e31e7ed7-bf87-4520-8483-5a8673026030'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definitions in definitions:
    print(definitions)
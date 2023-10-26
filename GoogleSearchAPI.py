import requests
import json
from secrets import API_KEY, SEARCH_ENGINE_ID

query = 'Apple M3 release date'
URL = "https://www.googleapis.com/customsearch/v1"


page = 1
for i in range(1):

    params = {
    'q': query,
    'key': API_KEY,
    'cx': SEARCH_ENGINE_ID,
    'hl': 'es',
    'cr': 'countryES',
    'start': str(page + i*10)
    #'fields': 'items'
} 
    response = requests.get(URL, params=params)
    results = response.json()

    for result in results['items']:
        print(result['link'])





import requests
import json

api_key = 'Tz9f45LJnj5G7tnbvwbT5s7InEQ8SVrz4sh0cRjK'
api_url = 'https://images-api.nasa.gov/search'



# Your search query here
search_query = 'earth'

params = {
    'q': search_query
}

response = requests.get(api_url, params=params)
data = response.json()

formatted_data = json.dumps(data, indent=20)

print(data)

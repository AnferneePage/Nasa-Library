from website import create_app
import requests
import json


api_key = 'Tz9f45LJnj5G7tnbvwbT5s7InEQ8SVrz4sh0cRjK'
api_url = 'https://images-api.nasa.gov/search'
search_query = 'rocks'


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

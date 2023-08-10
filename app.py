import requests
import json
from flask import Flask, render_template

app = Flask(__name__)

api_key = 'Tz9f45LJnj5G7tnbvwbT5s7InEQ8SVrz4sh0cRjK'
api_url = 'https://images-api.nasa.gov/search'
search_query = 'rocks'

@app.route('/')
def index():
    params = {'q': search_query}
    r = requests.get(api_url, params=params)
    data = r.json()
    
    return render_template('static/app.html', api_data=data)

if __name__ == '__main__':
    app.run()

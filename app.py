from flask import request, render_template
from website import create_app
import requests
import json


api_key = 'Tz9f45LJnj5G7tnbvwbT5s7InEQ8SVrz4sh0cRjK'
api_url = 'https://images-api.nasa.gov/search'

headers = {
    'api_key': api_key
}


def fetch_images(search_query):
    params = {
    'q': search_query
    }

    response = requests.get(api_url, headers=headers, params=params)
    data = data = json.loads(response.content)

    api_images = []
    items = data.get("collection", {}).get("items", [])
    for item in items:
        links = item["links"] if "links" in item else []
        if links:
            preview_link = links[0].get("href")
            api_images.append(preview_link)
            print(api_images)
    return api_images


app = create_app()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_query = request.form['user-input']
        print(search_query)
        api_images = fetch_images(search_query)
        return render_template('base.html', api_images=api_images, search_query=search_query)
    return render_template('base.html', api_images=[])

if __name__ == '__main__':
    app.run(debug=True)



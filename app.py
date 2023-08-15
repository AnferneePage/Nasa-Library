from flask import request, render_template
from website import create_app
import requests
import json


api_key = 'Tz9f45LJnj5G7tnbvwbT5s7InEQ8SVrz4sh0cRjK'
api_url = 'https://images-api.nasa.gov/search'

headers = {
    'api_key': api_key
}


def fetch_images_and_videos(search_query):
    params = {
        'q': search_query
    }

    response = requests.get(api_url, headers=headers, params=params)
    data = json.loads(response.content)

    api_media = {'images': [], 'videos': []}
    items = data.get("collection", {}).get("items", [])
    for item in items:
        media_type = item.get("data", [])[0].get("media_type")
        nasa_id = item.get("data", [])[0].get("nasa_id")
        links = item.get("links", [])
        if links:
            preview_link = links[0].get("href")
            if media_type == "image":
                api_media['images'].append(preview_link)
            elif media_type == "video":
                api_media['videos'].append({'nasa_id': nasa_id, 'preview_link': preview_link})
    return api_media



app = create_app()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_query = request.form['user-input']
        api_media = fetch_images_and_videos(search_query)
        videos_manifests = []

        for video in api_media['videos']:
            video_nasa_id = video['nasa_id']
            video_manifest_url = f"https://images-api.nasa.gov/asset/{video_nasa_id}"
            video_response = requests.get(video_manifest_url)
            video_manifest_data = json.loads(video_response.content)
            videos_manifests.append({'nasa_id': video_nasa_id, 'manifest': video_manifest_data})
            print(videos_manifests)

        return render_template('base.html', api_media=api_media, videos_manifests=videos_manifests, search_query=search_query)
    return render_template('base.html', api_media={'images': [], 'videos': []})


if __name__ == '__main__':
    app.run(debug=True)



from flask import request, render_template
from website import create_app
import requests
import json


app = create_app()

api_key = 'Tz9f45LJnj5G7tnbvwbT5s7InEQ8SVrz4sh0cRjK'
api_url = 'https://images-api.nasa.gov/search'
apod_api_url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

headers = {
    'api_key': api_key
}

def get_apod():
    parameters = {
        "date": "",  
        "hd": True  
    }

    res = requests.get(apod_api_url, params=parameters)
    d = res.json()
    # print(json.dumps(d, indent=4))
    modal_resources = {'title':'','image':'', 'desciption':''}
    modal_resources['title'] = d['title']
    modal_resources['image'] = d['hdurl']  
    modal_resources['description'] = d['explanation']
    return modal_resources





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






@app.route('/', methods=['GET', 'POST'])
def index():
    modal_resources=get_apod()

    if request.method == 'POST':
        search_query = request.form['user-input']
        api_media = fetch_images_and_videos(search_query)
        videos_manifests = []
        seen_links = set()

        for video in api_media['videos']:
            video_nasa_id = video['nasa_id']
            video_manifest_url = f"https://images-api.nasa.gov/asset/{video_nasa_id}"
            video_response = requests.get(video_manifest_url)
            video_manifest_data = json.loads(video_response.content)
            # print(video_manifest_data)
            videos_manifests.append({'nasa_id': video_nasa_id, 'manifest': video_manifest_data})
            # print(videos_manifests)
            

        return render_template('base.html', api_media=api_media,modal_resources=modal_resources, videos_manifests=videos_manifests, search_query=search_query)
    return render_template('base.html',modal_resources=modal_resources, api_media={'images': [], 'videos': []})





if __name__ == '__main__':
    get_apod()
    app.run(debug=True)
    



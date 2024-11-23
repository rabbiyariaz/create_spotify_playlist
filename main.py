import os

import requests
from spotipy import client
from spotipy.oauth2 import SpotifyOAuth
import dotenv
from bs4 import BeautifulSoup

dotenv.load_dotenv()
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
    "cookie": "REDACTED",  # Replace with the actual cookie during execution
    "user-agent": "Mozilla/5.0 (Your browser info here)",
}

url = "https://www.billboard.com/charts/hot-100/2023-10-20/"
response = requests.get(url, headers=headers)

# Check the response
if response.status_code == 200:
    print("Request successful!")

else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")



soup = BeautifulSoup(response.text, 'html.parser')

all_results = soup.select('div.o-chart-results-list-row-container')

list_of_tracks = []
list_of_tracks_uri = []

for index,result_info in enumerate(all_results):
    print("-------------------------------")
    title = result_info.select_one('h3#title-of-a-story').text.strip()
    list_of_tracks.append(title)

    image = result_info.select_one('img')['data-lazy-src']
    singer = result_info.select_one(
        'li.lrv-u-width-100p  ul.lrv-a-unstyle-list  li.o-chart-results-list__item span.c-label').text.strip()

sp_oauth = SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="playlist-modify-private",cache_path="token.txt"
)

url_code = sp_oauth.get_authorization_code()

token_info = sp_oauth.get_access_token(code=url_code, as_dict=True, check_cache=True)
access_token = token_info['access_token']

client = client.Spotify(auth=access_token)
user = client.current_user()

user_id = user['id']
for song in list_of_tracks:
    search = client.search(q=song, type="track", limit=1)
    try:
        uri = search["tracks"]["items"][0]["uri"]
        list_of_tracks_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

my_playlist = client.user_playlist_create(user=f"{user_id}", name="Billboard Top Tracks", public=False)
my_playlist_id = my_playlist['id']

tracks_addition = client.playlist_add_items(my_playlist_id, list_of_tracks_uri)
print(tracks_addition)

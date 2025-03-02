import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.getenv("CLT_ID")
CLIENT_S = os.getenv("CLT_S")
print(CLIENT_S)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth (
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_S,
        show_dialog=True,
        cache_path="token.txt",
        username= "Ankush" )
)
user_id = sp.current_user()["id"]

date = input("What year would you want to travel to (YYYY-MM-DD)? ")
URL = "https://www.billboard.com/charts/hot-100/" + date
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.text,'html.parser')
songs = soup.select('li ul li h3')
song_names = [name.getText().strip() for name in songs]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


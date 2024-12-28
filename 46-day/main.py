import spotipy
from bs4 import BeautifulSoup
import requests
from spotipy.oauth2 import SpotifyOAuth
year=input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
link=f"https://www.billboard.com/charts/hot-100/{year}"
response=requests.get(link)
soup=BeautifulSoup(response.text,"html.parser")
song_names = []
songs=soup.select("li ul li h3")
for title in songs:
    song_names.append(title.getText().strip())

spotify_auth = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope,
    username=username
))

user_id = spotify_auth.current_user()['id']
song_uris = []
year = year.split("-")[0]
for song in song_names:
    result = spotify_auth.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_uris)

playlist = spotify_auth.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)
print(playlist)

spotify_auth.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
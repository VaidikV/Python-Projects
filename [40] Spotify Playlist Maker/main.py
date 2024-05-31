import spotipy
from spotipy.oauth2 import SpotifyOAuth
# from spotipy.oauth2 import SpotifyAuthBase
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

# ------ Loading Env ------
load_dotenv("D:/Python/EnvironmentVariables/.env.txt")
SPTFY_CLIENTID = os.getenv("SPTFY_CLIENTID")
SPTFY_SECRET = os.getenv("SPTFY_SECRET")
SPTFY_REDIRECT_URI = "http://example.com"

# ------ Spotify auth setup using Spotipy ------

scope = "playlist-modify-private,playlist-modify-public"

auth_manager = SpotifyOAuth(client_id=SPTFY_CLIENTID,
                            client_secret=SPTFY_SECRET,
                            redirect_uri=SPTFY_REDIRECT_URI,
                            cache_path="token.txt",
                            scope=scope)

sp = spotipy.Spotify(auth_manager=auth_manager)

# ------ Asking the user to give a date ------

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]
month = date.split("-")[1]

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
data = response.text

# ------ Making a soup and fetching all the song names ------

soup = BeautifulSoup(data, "html.parser")

songs_tags = soup.find_all("span", class_="chart-element__information__song text--truncate color--primary")
artists_tags = soup.find_all("span",
                             class_="chart-element__information__artist text--truncate color--secondary")

songs = [song.getText() for song in songs_tags]

artists = [artist.getText() for artist in artists_tags]

date_in_words = soup.find("button", class_="date-selector__button button--link").getText().strip()

# ------ Get user id, get song uri, make new playlist, add songs, etc using Spotipy ------

user_id = sp.me()["id"]

index = 0
all_songs_uri = []

for song in songs:
    query = f"{song} {artists[index].split()[-1]}"
    try:
        need = sp.search(q=query, type="track", limit=2, market="US")["tracks"]["items"][0]["uri"]
    except IndexError:
        try:
            need = sp.search(q=f"{song} {artists[index].split()[0]} ",
                             type="track", market="US")["tracks"]["items"][0]["uri"]
            print(f"Exception triggered for \"{song}\". First name of the artist used instead.")
        except IndexError:
            need = sp.search(q=f"{song}",
                             type="track")["tracks"]["items"][0]["uri"]
            print(f"The song \"{song}\" was added by searching only by it's name. This is possible "
                  f"because the artist name inclusion leads to no result. There is a chance that the downloaded "
                  f"song might be wrong. Please check it.")
    all_songs_uri.append(need)
    index += 1

new_playlist = sp.user_playlist_create(user=user_id,
                                       name=f"Billboard Hot 100 ({month}/{year}) ",
                                       public=True,
                                       description=f"Billboard Hot 100 tracks on {date_in_words}")

add_tracks = sp.playlist_add_items(new_playlist["id"], all_songs_uri)


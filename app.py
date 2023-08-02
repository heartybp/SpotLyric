import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius
from flask import Flask, render_template, request

app = Flask(__name__)

def authenticate_spotify():
    # Replace with your Spotify API credentials !!

    client_id = "YOUR-CLIENT-ID"
    client_secret = "YOUR-CLIENT-SECRET"

    client_credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials)
    return sp

def search_song(sp, song_name):
    results = sp.search(q=song_name, type='track', limit=20)
    return results['tracks']['items']

def get_track_details(sp, track_id):
    track = sp.track(track_id)

    # Fetch lyrics using LyricsGenius API
    
    # Replace with your Genius API token
    genius_token = "YOUR-GENIUS-TOKEN" 
    genius = lyricsgenius.Genius(genius_token)
    song = genius.search_song(track["name"], track["artists"][0]["name"])

    # Add the lyrics to the track details dictionary
    if song:
        track["lyrics"] = song.lyrics
    else:
        track["lyrics"] = "Lyrics not found for this song."

    return track

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        spotify_api = authenticate_spotify()
        search_query = request.form["search_query"]
        songs = search_song(spotify_api, search_query)

        if songs:
            return render_template("results.html", songs=songs)
        else:
            return render_template("results.html", error="No songs found for the given search query.")
    return render_template("index.html")

@app.route("/song/<track_id>")
def song_details(track_id):
    spotify_api = authenticate_spotify()
    track = get_track_details(spotify_api, track_id)

    return render_template("details.html", track=track)

@app.route("/details/<track_id>")
def song_details_page(track_id):
    spotify_api = authenticate_spotify()
    track = get_track_details(spotify_api, track_id)
    return render_template("details.html", track=track)

if __name__ == "__main__":
    app.run(debug=True)
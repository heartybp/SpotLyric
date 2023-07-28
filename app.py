# import Spotipy and SpotifyClientCredentials to communicate with Spotify API

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask, render_template, request

def authenticate():
    client_id = "YOUR-CLIENT-ID"
    client_secret = "YOUR-CLIENT-SECRET"

    client_credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials)
    return sp

def search_song(sp, song):
    search_list = sp.search(q=song, type='track', limit=10)
    return search_list['tracks']['items']

# 'tracks' and 'items' are key names used in the JSON response returned by the Spotify API when you perform a search query for tracks
# -- return results['tracks']['items'] -- searches for matching items in spotify's dictionary of songs

def get_track_details(sp, track_id):
    track = sp.track(track_id)
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

    return render_template("song_details.html", track=track)

if __name__ == "__main__":
    app.run(debug=True)


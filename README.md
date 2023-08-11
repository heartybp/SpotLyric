# SpotLyric
SpotLyric is a web application that allows users to search for their favorite songs. The app integrates the Spotify and Genius API using the Spotipy and LyricsGenius libraries in order to fetch song details and lyrics.

Users are able to search for a song and receive a list of matching results. 
Users can then select the desired search result and view more detailed information about the song such as the album, release date, and popularity.
Lyrics for the song are displayed on the song information page.
Embedded song previews are also available for listening. 

## SpotLyric Video Demo
Note: Turn audio on to hear song demos
https://github.com/heartybp/SpotLyric/assets/98626381/62e85603-f44c-42e3-8ae5-70a381a8d5a2

### Technologies:
* Python: Developed the backend and included API integration.
* Flask: Used to create the web application and handle user requests.
* [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/): Python library that interacts with the Spotify Web API and retrieve song information.
* [LyricsGenius](https://lyricsgenius.readthedocs.io/en/master/): Python client for Genius API - used to fetch lyrics for the selected song.
* HTML/CSS: Designed the frontend of the application using HTML and CSS.

Application Features: search functionality, integrated audio player
  
### Notes:
Known Issues:
The Genius API response displays additional content in the lyrics section such as contributor information and language translations. 

I removed my personal Spotify client ID + secret and Genius API token from uploaded GitHub code.<br>

To run this application using Visual Studio Code:
  * Download source files and open using VSCode
  * Replace your Spotify client ID + secret and Genius token in app.py
  * Initialize a virtual environment
    ```python -m venv .venv```
  * In the virtual environment, install spotipy and Flask ```pip install spotipy``` ```pip install Flask```
  * Run Flask ```flask run```




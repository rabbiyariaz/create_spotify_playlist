# Billboard Hot 100 to Spotify Playlist
This Python script fetches the Billboard Hot 100 chart from a specified date and creates a Spotify playlist with the top songs from the chart. The script utilizes the Spotify API to authenticate, search for songs, and manage playlists and uses BeautifulSoup for web scraping.
## Features
Fetches the Billboard Hot 100 chart for a specific date.
Extracts song titles and corresponding artist names from the chart.
Searches for these songs on Spotify.
Creates a private Spotify playlist and adds the fetched songs.
## Setup and Prerequisites
### 1. Clone the Repository
git clone https://github.com/your-username/create_spotify_playlist.git
cd create_spotify_playlist

### 2. Install Required Libraries
pip install requests spotipy python-dotenv beautifulsoup4
### 3. Spotify Developer Application
Go to the Spotify Developer Dashboard.
Create a new app and note the Client ID and Client Secret.
Set a redirect URI (e.g., http://localhost:8888/callback).
### 4. Create a .env File
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback





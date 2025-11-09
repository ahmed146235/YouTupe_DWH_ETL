import requests
import json
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")
API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE = "MrBeast"

def get_playlist_id():
    try:
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        channel_items = data['items'][0]
        channel_playlistID= channel_items['contentDetails']['relatedPlaylists']['uploads']
        print(channel_playlistID)
        return channel_playlistID
    except requests.exceptions.RequestException as e:
        raise e
    
if __name__ == "__main__":
    get_playlist_id()


"""
import requests

def get_playlist_id(api_key, channel_handle):
    try:
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={channel_handle}&key={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        playlist_id = data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        return playlist_id
    except requests.exceptions.RequestException as e:
        raise e

if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY"
    CHANNEL_HANDLE = "MrBeast"
    print(get_playlist_id(API_KEY, CHANNEL_HANDLE))

    """

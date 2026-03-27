import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

def create_spotify_client():
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

    if not client_id or not client_secret:
        raise ValueError("Spotify Client ID or Secret not found in .env")

    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(auth_manager=auth_manager)

sp = create_spotify_client()

class SpotifyServiceException(Exception):
    pass

def get_recommendations(genres: list, limit=5):
    if not genres:
        genres = ["pop"]  # fallback
    
    recommendations = []

    # Search tracks by genre keyword until we reach the limit
    for genre in genres:
        try:
            results = sp.search(q=f'genre:"{genre}"', type='track', limit=limit)
            for item in results['tracks']['items']:
                recommendations.append({
                    "name": item["name"],
                    "artist": item["artists"][0]["name"],
                    "url": item["external_urls"]["spotify"]
                })
            if len(recommendations) >= limit:
                break
        except Exception as e:
            raise SpotifyServiceException(f"Spotify API search failed for genre '{genre}': {e}")

    return recommendations[:limit] if recommendations else [{
        "name": "No tracks found",
        "artist": "",
        "url": ""
    }]

# Quick test
if __name__ == "__main__":
    print("Testing Spotify service...")
    try:
        test_songs = get_recommendations(["pop", "dance"], limit=3)
        for s in test_songs:
            print(s["name"], "-", s["artist"], "-", s["url"])
    except SpotifyServiceException as e:
        print(e)

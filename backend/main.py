from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from models.emotion_classifier import analyze_emotion
from utils.emotion_to_genre import map_emotion_to_genres
from services.spotify_service import get_recommendations

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://emotion-music-app-beige.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # or ["*"] if you want to allow everything
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    text: str

@app.post("/analyze")
def analyze(user_input: UserInput):
    # Step 1: Analyze emotion
    emotion = analyze_emotion(user_input.text)

    # Step 2: Map to genres
    genres = map_emotion_to_genres(emotion)

    # Step 3: Get Spotify songs
    try:
        songs = get_recommendations(genres)
    except Exception as e:
        # fallback: return empty list instead of crashing
        songs = []
    
    return {
        "emotion": emotion,
        "genres": genres,
        "songs": songs
    }


@app.get("/test")
def test():
    return {"message": "Backend is running"}

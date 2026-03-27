def map_emotion_to_genres(emotion: str):
    emotion = emotion.lower()
    
    # Emotion → Spotify seed genres mapping (all valid)
    mapping = {
        "joy": ["pop", "dance", "happy"],          # all valid
        "anger": ["metal", "rock"],                # all valid
        "sadness": ["acoustic", "piano", "chill"],# all valid
        "fear": ["ambient", "classical"],          # all valid
        "neutral": ["indie", "jazz"],             # all valid
    }

    # Spotify allowed seed genres
    VALID_GENRES = [
        "acoustic", "afrobeat", "alt-rock", "alternative", "ambient", "anime", "black-metal",
        "blues", "bossanova", "brazil", "breakbeat", "british", "cantopop", "chill", "classical",
        "club", "comedy", "country", "dance", "dancehall", "deep-house", "disco", "drum-and-bass",
        "dub", "dubstep", "edm", "electro", "electronic", "emo", "folk", "forro", "funk",
        "garage", "gospel", "goth", "grindcore", "groove", "grunge", "guitar", "happy", "hard-rock",
        "hardcore", "hardstyle", "heavy-metal", "hip-hop", "house", "indie", "indie-pop", "industrial",
        "j-dance", "j-idol", "j-pop", "j-rock", "jazz", "k-pop", "kids", "latin", "latino", "malay",
        "mandopop", "metal", "metal-misc", "metalcore", "minimal-techno", "movies", "mpb",
        "new-age", "new-release", "opera", "pagan", "party", "piano", "pop", "pop-film",
        "post-dubstep", "power-pop", "progressive-house", "psych-rock", "punk", "punk-rock",
        "r-n-b", "reggae", "reggaeton", "rock", "rock-n-roll", "rockabilly", "romance", "sad",
        "samba", "sertanejo", "show-tunes", "singer-songwriter", "ska", "sleep", "songwriter",
        "soul", "soundtracks", "spanish", "study", "summer", "synth-pop", "techno", "trance",
        "trip-hop", "vocal", "world"
    ]

    # Filter out any invalid genres (extra safety)
    genres = [g for g in mapping.get(emotion, ["pop"]) if g in VALID_GENRES]
    
    # Fallback if none valid
    if not genres:
        genres = ["pop"]
        
    return genres

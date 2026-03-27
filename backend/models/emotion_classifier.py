from transformers import pipeline

# Load a Hugging Face emotion model
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

def analyze_emotion(text: str) -> str:
    result = classifier(text)[0][0]   # top prediction
    return result["label"].lower()

from typing import Dict, List
import os
from dotenv import load_dotenv

def load_environment():
    """Load environment variables from .env file."""
    load_dotenv()
    required_vars = ['SPOTIFY_CLIENT_ID', 'SPOTIFY_CLIENT_SECRET']
    missing = [var for var in required_vars if not os.getenv(var)]
    if missing:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing)}")

def get_mood_music_parameters(mood: str) -> Dict[str, any]:
    """
    Get music parameters based on mood.
    Returns dictionary with parameters like tempo, energy, valence.
    """
    mood_params = {
        'happy': {
            'min_tempo': 120,
            'target_energy': 0.8,
            'target_valence': 0.8,
            'genres': ['pop', 'dance', 'happy']
        },
        'sad': {
            'min_tempo': 60,
            'target_energy': 0.3,
            'target_valence': 0.2,
            'genres': ['acoustic', 'sad', 'piano']
        },
        'angry': {
            'min_tempo': 140,
            'target_energy': 0.9,
            'target_valence': 0.4,
            'genres': ['rock', 'metal', 'intense']
        },
        'neutral': {
            'min_tempo': 90,
            'target_energy': 0.5,
            'target_valence': 0.5,
            'genres': ['ambient', 'chill']
        },
        'surprise': {
            'min_tempo': 110,
            'target_energy': 0.7,
            'target_valence': 0.7,
            'genres': ['electronic', 'pop']
        },
        'fear': {
            'min_tempo': 80,
            'target_energy': 0.4,
            'target_valence': 0.3,
            'genres': ['ambient', 'atmospheric']
        },
        'disgust': {
            'min_tempo': 100,
            'target_energy': 0.6,
            'target_valence': 0.3,
            'genres': ['rock', 'alternative']
        }
    }
    return mood_params.get(mood, mood_params['neutral'])

def format_mood_name(mood: str) -> str:
    """Format mood name for display."""
    return mood.lower().strip() 
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from typing import Dict, List, Optional

class SpotifyController:
    def __init__(self):
        self.sp = self._initialize_spotify()
        self.current_playlist_id = None

    def _initialize_spotify(self) -> spotipy.Spotify:
        """Initialize Spotify client with necessary permissions."""
        scope = "user-read-playback-state user-modify-playback-state playlist-modify-public"
        return spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv('SPOTIFY_CLIENT_ID'),
            client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
            redirect_uri="http://localhost:8888/callback",
            scope=scope
        ))

    def create_mood_playlist(self, mood: str, tracks: List[str]) -> Optional[str]:
        """
        Create a new playlist based on mood and add tracks.
        Args:
            mood: String representing the current mood
            tracks: List of Spotify track URIs
        Returns:
            Playlist ID if successful, None otherwise
        """
        try:
            user_id = self.sp.current_user()['id']
            playlist = self.sp.user_playlist_create(
                user_id,
                f"Mood DJ - {mood.capitalize()}",
                public=False,
                description=f"Generated playlist for {mood} mood"
            )
            
            if tracks:
                self.sp.playlist_add_items(playlist['id'], tracks)
            
            self.current_playlist_id = playlist['id']
            return playlist['id']
        except Exception as e:
            print(f"Error creating playlist: {str(e)}")
            return None

    def play_mood_music(self, playlist_id: str) -> bool:
        """
        Start playback of the specified playlist.
        Args:
            playlist_id: Spotify playlist ID to play
        Returns:
            True if playback started successfully, False otherwise
        """
        try:
            self.sp.start_playback(context_uri=f"spotify:playlist:{playlist_id}")
            return True
        except Exception as e:
            print(f"Error starting playback: {str(e)}")
            return False

    def get_mood_tracks(self, mood: str, limit: int = 20) -> List[str]:
        """
        Search for tracks matching the given mood.
        Args:
            mood: String representing the mood
            limit: Maximum number of tracks to return
        Returns:
            List of Spotify track URIs
        """
        search_terms = {
            'happy': 'happy upbeat energetic',
            'sad': 'sad melancholic',
            'angry': 'intense aggressive',
            'neutral': 'calm relaxing',
            'surprise': 'exciting uplifting',
            'fear': 'atmospheric ambient',
            'disgust': 'dark intense'
        }

        try:
            results = self.sp.search(
                q=search_terms.get(mood, mood),
                type='track',
                limit=limit
            )
            return [track['uri'] for track in results['tracks']['items']]
        except Exception as e:
            print(f"Error searching tracks: {str(e)}")
            return [] 
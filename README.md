# Mood DJ 🎵 😊

A smart music player that detects your mood through computer vision and automatically plays appropriate music through Spotify.

## Features 🌟

- Real-time mood detection through webcam
- Automatic playlist generation based on detected mood
- Spotify integration for music playback
- Customizable mood-to-music mappings
- Visual emotion analysis with confidence scores

## Demo 📸

The project includes a test script that shows real-time emotion detection with confidence scores and visual bars:
```bash
python test_mood_detector.py
```

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Mood_DJ.git
cd Mood_DJ
```

2. Create and activate a virtual environment:
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
.\venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up Spotify API credentials:
   - Create a [Spotify Developer account](https://developer.spotify.com/)
   - Create a new application
   - Set the environment variables in a `.env` file:
     ```
     SPOTIFY_CLIENT_ID=your_client_id
     SPOTIFY_CLIENT_SECRET=your_client_secret
     ```

## Usage 💻

1. Run the test script to check emotion detection:
```bash
python test_mood_detector.py
```

2. Run the main application:
```bash
python app.py
```

## Requirements 📋

- Python 3.11+
- Webcam access
- Spotify Premium account
- Internet connection

## Project Structure 📁

```
mood_dj/
├── app.py                 # Main application
├── mood_detector.py       # Computer vision module
├── spotify_controller.py  # Spotify API interface
├── test_mood_detector.py # Visual testing script
├── utils.py              # Helper functions
├── requirements.txt      # Dependencies
└── README.md            # Documentation
```

## Contributing 🤝

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- [DeepFace](https://github.com/serengil/deepface) for emotion detection
- [Spotipy](https://spotipy.readthedocs.io/) for Spotify integration
- OpenCV for computer vision capabilities 
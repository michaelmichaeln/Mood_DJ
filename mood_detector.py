import cv2
from deepface import DeepFace
from typing import Optional, Dict

def detect_mood() -> Optional[str]:
    """
    Detect the dominant emotion from webcam capture.
    Returns:
        str: The dominant emotion detected ('happy', 'sad', etc.) or None if detection fails
    """
    cap = cv2.VideoCapture(0)
    try:
        if not cap.isOpened():
            print("Error: Could not open video device")
            return None
        
        # Try to get a frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            return None

        # Analyze the frame for emotions
        analysis = DeepFace.analyze(
            frame,
            actions=['emotion'],
            enforce_detection=False
        )
        
        # Handle both single and list results from DeepFace
        if isinstance(analysis, list):
            analysis = analysis[0]
        
        return analysis['dominant_emotion']

    except Exception as e:
        print(f"Error during mood detection: {str(e)}")
        return None
    
    finally:
        # Always ensure the camera is released
        cap.release()

def get_all_emotions() -> Optional[Dict[str, float]]:
    """
    Get all emotion probabilities from webcam capture.
    Returns:
        Dict[str, float]: Dictionary of emotions and their probabilities or None if detection fails
    """
    cap = cv2.VideoCapture(0)
    try:
        if not cap.isOpened():
            print("Error: Could not open video device")
            return None
        
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            return None

        analysis = DeepFace.analyze(
            frame,
            actions=['emotion'],
            enforce_detection=False
        )
        
        if isinstance(analysis, list):
            analysis = analysis[0]
        
        return analysis['emotion']

    except Exception as e:
        print(f"Error during emotion detection: {str(e)}")
        return None
    
    finally:
        cap.release()


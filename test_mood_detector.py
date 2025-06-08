import cv2
from deepface import DeepFace
import numpy as np

def draw_text(img, text, position, color=(255, 255, 255)):
    """Draw text with a dark background for better visibility"""
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7
    thickness = 2
    padding = 5

    # Get text size
    (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, thickness)
    
    # Draw background rectangle
    cv2.rectangle(img, 
                 (position[0] - padding, position[1] - text_height - padding),
                 (position[0] + text_width + padding, position[1] + padding),
                 (0, 0, 0), 
                 -1)
    
    # Draw text
    cv2.putText(img, text, position, font, font_scale, color, thickness)

def draw_emotion_bar(img, emotion, score, position, max_width=150):
    """Draw a bar representing emotion strength"""
    bar_height = 15
    bar_color = (120, 120, 120)
    fill_color = (0, 255, 0)  # Green for the filled portion
    
    # Draw the empty bar
    cv2.rectangle(img,
                 (position[0], position[1] - bar_height),
                 (position[0] + max_width, position[1]),
                 bar_color,
                 1)
    
    # Draw the filled portion
    filled_width = int(max_width * (score / 100))
    if filled_width > 0:
        cv2.rectangle(img,
                     (position[0], position[1] - bar_height),
                     (position[0] + filled_width, position[1]),
                     fill_color,
                     -1)

def main():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open video device")
        return

    print("Press 'q' to quit")
    
    try:
        while True:
            # Read frame
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame")
                break

            try:
                # Analyze emotions
                analysis = DeepFace.analyze(frame, 
                                         actions=['emotion'],
                                         enforce_detection=False,
                                         silent=True)
                
                if isinstance(analysis, list):
                    analysis = analysis[0]

                # Get emotion scores
                emotion_scores = analysis['emotion']
                dominant_emotion = analysis['dominant_emotion']
                
                # Sort emotions by score
                sorted_emotions = sorted(emotion_scores.items(), key=lambda x: x[1], reverse=True)

                # Draw title
                draw_text(frame, "Emotion Analysis:", (10, 30), (255, 255, 255))
                
                # Draw dominant emotion
                draw_text(frame, f"Dominant: {dominant_emotion.upper()}", (10, 60), (0, 255, 0))

                # Draw all emotions with bars
                y_pos = 90
                for emotion, score in sorted_emotions:
                    # Format the text with fixed width for better alignment
                    text = f"{emotion:<8}: {score:>6.1f}%"
                    color = (0, 255, 0) if emotion == dominant_emotion else (255, 255, 255)
                    draw_text(frame, text, (10, y_pos), color)
                    
                    # Draw bar graph
                    draw_emotion_bar(frame, emotion, score, (200, y_pos))
                    
                    y_pos += 30

            except Exception as e:
                # If face detection fails, just show the frame
                draw_text(frame, "No face detected", (10, 30), (0, 0, 255))

            # Show the frame
            cv2.imshow('Mood Detector Test', frame)

            # Break loop on 'q' press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # Clean up
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main() 

import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
import streamlit as st

@st.cache_data
@st.cache_resource
def analyze_image(img_path):
    
    analysis = DeepFace.analyze(
        img_path=img_path, enforce_detection=False, detector_backend="mtcnn", actions=["age", "gender", "emotion", "race"]
    )

    def draw_regions_on_image(image, region_list, color=(0, 0, 255), thickness=10):
        img_with_rectangles = image.copy()

        for item in region_list:
            region = item.get('region')
            if region:
                x1, y1, w, h = region['x'], region['y'], region['w'], region['h']
                cv2.rectangle(img_with_rectangles, (x1, y1), (x1 + w, y1 + h), color, thickness)

        return img_with_rectangles

    # Load your image
    img = cv2.imread(img_path)

    # Create a copy of the image to draw the rectangle on
    img_with_rectangle = img.copy()
    # List of dictionaries with "region" keys
    region_data = analysis
    # Draw the rectangles on the image
    img_with_rectangle = draw_regions_on_image(img, region_data, (255, 0, 0), 10)
    
    # Display the image with rectangles using Streamlit
    st.image(img_with_rectangle, channels="BGR", use_column_width=True)
    
    emotion = analysis[0]['dominant_emotion']
    age = analysis[0]['age']
    gender = analysis[0]['dominant_gender']
    race = analysis[0]['dominant_race']
    
    return emotion, age, gender, race, analysis


def emotion_translator(emotion):
    # Define the English to Spanish emotion translation dictionary
    emotion_translation = {
        "happy": "Alegría",
        "sad": "Tristeza",
        "angry": "Enfado",
        "surprise": "Sorpresa",
        "fear": "Susto",
        "disgust": "Disgusto",
        "neutral": "Neutro"
    }
    translation = emotion_translation.get(emotion, emotion)
    
    return translation
    
def emotion_to_emoji(emotion):
    # Define the emotion to emoji translation dictionary
    emotion_emoji = {
        "happy": "😄",
        "sad": "😢",
        "angry": "😡",
        "surprise": "😲",
        "fear": "😨",
        "disgust": "🤢",
        "neutral": "😐"
    }
    emoji = emotion_emoji.get(emotion, "Unknown Emoji")  # Default to "Unknown Emoji" if not found

    return emoji

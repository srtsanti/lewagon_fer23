import streamlit as st
from app.detect_face import detector

import os
import tempfile
import matplotlib.pyplot as plt
import requests
from PIL import Image
from io import BytesIO

from app.deep_face  import analyze_image

# Create a sidebar with page selection
page = st.sidebar.radio("Select a page", ["Inteligencia Emocional Artifiacial" , "Detector de Emociones"])

def main():
    
    # Center the title using CSS
    st.markdown(
        f"""
        <h1 style='text-align: center;'>
            Inteligencia [EMOCIONAL] Artificial
        </h1>
        """,
        unsafe_allow_html=True
    )

    # Center a subtitle with a specific CSS class
    st.markdown(
        f"""
        <h4 style='text-align: center;'>
            Bienvenido a la aplicacion de Reconocimiento facial emocional!
        </h4>
        """,
        unsafe_allow_html=True
    )

    #GIF
    # Specify the desired width for the image (e.g., 300 pixels)
    desired_width = 400
    gif_url = "https://media.giphy.com/media/26n6xoDuf7OF0cGIM/giphy.gif"
    # Display the image with custom HTML to adjust the size and center it
    centered_html = f"""
    <div style="display: flex; justify-content: center;">
        <img src="{gif_url}" width="{desired_width}">
    </div>
    """
    st.markdown(centered_html, unsafe_allow_html=True)
    
    st.write("---------------")
    
    # Create a layout with two columns
    left_column, right_column = st.columns(2)
    # Right column
    with right_column:
        st.write("")
       
        
    

# Display the selected page
if page == "Inteligencia Emocional Artifiacial":
    main()
elif page == 'Detector de Emociones':
    detector()


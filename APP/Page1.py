import streamlit as st

import os
import tempfile
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from PIL import Image
from io import BytesIO

from deep_face  import analyze_image, emotion_translator

def detector():
    st.markdown("### Seleccione una Imagen")
    image_source = st.radio("Elige la fuente de la imagen", ["Desde el ordenador", "Pegue una URL", "Saque una foto (solo para movil)"])

    if image_source == "Desde el ordenador":
        st.write("Seleccione una imagen desde su ordenador:")
        uploaded_file = st.file_uploader("Upload a picture", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            st.image(uploaded_file, use_column_width=False, width=150)
            
        prediction_button = st.button("Predict")
        
        if prediction_button:
            if uploaded_file is not None:
                # Create a temporary directory to store the uploaded file
                temp_dir = tempfile.TemporaryDirectory()
                temp_file_path = os.path.join(temp_dir.name, uploaded_file.name)

                # Save the uploaded file to the temporary location
                with open(temp_file_path, "wb") as f:
                    f.write(uploaded_file.read())

                col1, col2 = st.columns(2)
                with col1:
                    emotion, age, gender, race, analysis = analyze_image(temp_file_path)
                    # Clean up the temporary directory
                    temp_dir.cleanup()
                    spanish_emotion = emotion_translator(emotion)
                    st.markdown(f"## Emocion Detectada: {spanish_emotion}")
                    # st.write(f"Predicted Age: {age}")
                    # st.write(f"Predicted Gender: {gender}")
                with col2:        
                    # Add the PLOT
                    data = analysis[0]['emotion']
                    spanish_emotion_names = [emotion_translator(emotion) for emotion in data.keys()]
                    percentages = list(data.values())
                    st.write(" ")  
                    st.write(" ")  
                    st.write(" ")  
                    st.write(" ") 
                    st.write(" ")  
                    st.write(" ") 
                    st.markdown(f'#### Distribucion de Emociones')

                    # Create a bar plot using seaborn
                    plt.figure(figsize=(12, 10))
                    sns.barplot(x=percentages, y=spanish_emotion_names, palette='dark')
                    plt.xlabel('Porcentaje')
                    plt.ylabel('Emocion')
                    plt.title('Distribucion de Emociones')
                    st.pyplot(plt)

    elif image_source == "Pegue una URL":  # User chose "Paste URL"
        url = st.text_input("Pegue la URL de la imagen")
        if url:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    image = Image.open(BytesIO(response.content))
                    st.image(image, use_column_width=False, width=150)
                    
                    st.write(" ") 
                    
                    prediction_button = st.button("Predict")
                    st.write(" ") 
                    if prediction_button:
                        # Save the image to a temporary location
                        temp_dir = tempfile.TemporaryDirectory()
                        temp_file_path = os.path.join(temp_dir.name, "temp_image.jpg")
                        image.save(temp_file_path)
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            emotion, age, gender, race, analysis = analyze_image(temp_file_path)
                            # Clean up the temporary directory
                            temp_dir.cleanup()
                            spanish_emotion = emotion_translator(emotion)
                            st.markdown(f"## Emocion Detectada: {spanish_emotion}")
                            # st.write(f"Predicted Age: {age}")
                            # st.write(f"Predicted Gender: {gender}")
                        with col2:        
                            # Add the PLOT
                            data = analysis[0]['emotion']
                            spanish_emotion_names = [emotion_translator(emotion) for emotion in data.keys()]
                            percentages = list(data.values())
                            st.write(" ")  
                            st.write(" ") 
                            st.markdown(f'#### Distribucion de Emociones')

                            # Create a bar plot using seaborn
                            plt.figure(figsize=(12, 10))
                            sns.barplot(x=percentages, y=spanish_emotion_names, palette='dark')
                            plt.xlabel('Porcentaje')
                            plt.ylabel('Emocion')
                            plt.title('Distribucion de Emociones')
                            st.pyplot(plt)
                        
                else:
                    st.write("No es posible cargar esta image desde la URL.")
            except Exception as e:
                st.write(f"Error : {str(e)}")
    else:
        st.write("Haga click en el boton para sacar una foto:")
        image = st.camera_input("Capturar Imagen", label_visibility='hidden')
         
        if image is not None:        
            st.write(" ")          
            prediction_button = st.button("Predict")    
            if prediction_button:
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_file_path = os.path.join(temp_dir, "temp_image.jpg")
                    # Convert and save the captured image
                    # Convert and save the captured image
                    image_pil = Image.open(image)
                    image_pil.save(temp_file_path)
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        emotion, age, gender, race, analysis = analyze_image(temp_file_path)
                        spanish_emotion = emotion_translator(emotion)
                        st.markdown(f"## Emocion Detectada: {spanish_emotion}")
                        # st.write(f"Predicted Age: {age}")
                        # st.write(f"Predicted Gender: {gender}")
                        
                    with col2:        
                        # Add the PLOT
                        data = analysis[0]['emotion']
                        spanish_emotion_names = [emotion_translator(emotion) for emotion in data.keys()]
                        percentages = list(data.values())
                        st.write(" ")  
                        st.write(" ")  
                        st.write(" ")  
                        st.write(" ") 
                        st.write(" ")  
                        st.write(" ") 
                        st.markdown(f'#### Distribucion de Emociones')

                        # Create a bar plot using seaborn
                        plt.figure(figsize=(12, 10))
                        sns.barplot(x=percentages, y=spanish_emotion_names, palette='dark')
                        plt.xlabel('Porcentaje')
                        plt.ylabel('Emocion')
                        plt.title('Distribucion de Emociones')
                        st.pyplot(plt)

                        # plt.bar(list(emotion_translator(emotion) for emotion in data.keys()), list(data.values()))
                        # plt.xlabel('Emocion')
                        # plt.ylabel('Porcentaje')
                        # plt.title('Distribucion de Emociones')
                        # st.pyplot(plt)

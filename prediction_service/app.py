import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

'''
# Deep Classifier Project
'''

model = tf.keras.models.load_model('model.h5')

files_to_be_uploaded = st.file_uploader("Choose a file", accept_multiple_files=True)

for file_to_be_uploaded in files_to_be_uploaded:
    if file_to_be_uploaded is not None:
        
        image = Image.open(file_to_be_uploaded)
        image_array = image.resize((224,224))
        image_array = np.array(image_array)
        image_array = np.expand_dims(image_array, 0)

        prediction = model.predict(image_array)
        
        if np.argmax(prediction, 1) == 0:
            caption = 'Cat'
        else:
            caption = 'Dog'
        st.image(image, caption=caption)

    

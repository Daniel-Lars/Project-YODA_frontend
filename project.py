import os
from PIL import Image, ImageEnhance
import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
import time

@st.cache
def load_image(img):
    im = Image.open(img)
    return im

def main():
    "" 'Lego Prediction App'""

st.title('Lego Prediction App')
st.text('Built by Jacob, Daniel, Hicham and Yiping')
activities = st.sidebar.selectbox(
    "Select Activity", ("Lego Detection", "Lego Generation",))

if activities == "Lego Detection":
    st. subheader("Lego Detection")

    image_file = st.file_uploader("Upload Image", type=['JPEG','JPG'])
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
    my_bar.progress(percent_complete + 1)
    if image_file is not None:
        our_image = Image.open(image_file)
        st.image(our_image)
        st.write('This is ____')

elif activities == "Lego Generation":
    st.subheader("Lego Generation")

    image_file = st.file_uploader("Upload Image", type=['JPEG', 'JPG'])
    generation_type = st.sidebar.radio('Generation Type',['Original', 'Cartoon', 'GIF'])


if __name__ == '__main__':
    main()

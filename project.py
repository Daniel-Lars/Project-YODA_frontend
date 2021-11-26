import os

from PIL import Image
import streamlit as st
import base64
import pandas as pd
import numpy as np
from random import randrange
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
    "Select Activity", ("Lego Detection", "Yoda Maker",))

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

    st.sidebar.image("/Users/ypzhang/code/Daniel-Lars/yoda_sidebar.png",
                     use_column_width=True)

elif activities == "Yoda Maker":
    st.markdown("""
                Yoda Maker

                This app allows you to build your own Yoda based on the templates provided herein.""")
    st.sidebar.header("Customize Your Yoda")

    list_skin_color = ['tanned', 'yellow', 'pale', 'light', 'brown', 'dark_brown', 'black']
    list_facial_hair = ['default', 'beard_medium', 'beard_light', 'moustache_fancy']
    list_mouth_type = ['default', 'concerned', 'disbelief', 'eating', 'grimace', 'sad','scream_open', 'serious', 'smile', 'tongue', 'twinkle', 'vomit']
    list_eye_type = ['default', 'close', 'cry', 'dizzy', 'eye_roll', 'happy', 'hearts','surprised', 'wink']
    list_clothes_type = ['blazer_shirt', 'blazer_sweater', 'collar_sweater', 'hoodie','overall', 'shirt_crew_neck', 'shirt_v_neck']
    list_clothes_color = ['black', 'blue_01', 'blue_02', 'gray_01', 'gray_02', 'heather']

    index_skin_color = randrange(0, len(list_skin_color) )
    index_facial_hair_type = randrange(0, len(list_facial_hair) )
    index_mouth_type = randrange(0, len(list_mouth_type) )
    index_eye_type = randrange(0, len(list_eye_type) )
    index_clothe_type = randrange(0, len(list_clothes_type) )
    index_clothe_color = randrange(0, len(list_clothes_color) )

    option_skin_color = st.sidebar.selectbox('Skin',list_skin_color, index=index_skin_color)
    option_facial_hair = st.sidebar.selectbox('Facial Hair',list_facial_hair, index=index_facial_hair_type)
    option_mouth_type = st.sidebar.selectbox('Mouth Type', list_mouth_type, index=index_mouth_type)
    option_eye_type = st.sidebar.selectbox('Eye type', list_eye_type, index=index_eye_type)
    option_clothes_type = st.sidebar.selectbox('Clothes',list_clothes_type,index=index_clothe_type)
    option_clothes_color = st.sidebar.selectbox('Clothes Color',list_clothes_color,index=index_clothe_color)


    # avatar = pa.PyAvataaar(
    # skin_color=eval('pa.AvatarStyle.%s' % option_skin_color),
    # facial_hair_type=eval('pa.FacialHairType.%s' % option_facial_hair),
    # mouth_type=eval('pa.MouthType.%s' % option_mouth_type),
    # eye_type=eval('pa.EyesType.%s' % option_eye_type),
    # clothe_type=eval('pa.ClotheType.%s' % option_clothes_type),
    # color_type=eval('pa.ClotheClor.%s' % option_clothes_color)) """

    def imagedownload(filename):
        image_file = open(filename, 'rb')
        b64 = base64.b64encode(image_file.read()).decode()
        href = f'<a href="data:image/png;base64,{b64}" download={filename}>Download {filename} File</a>'
        return href

    st.subheader('**Rendered Avatar**')
    # rendered_avatar = avatar.render_png_file('Baby-Yoda.png')
    image = Image.open('Baby-Yoda.png')
    st.image(image)
    st.markdown(imagedownload('Baby-Yoda.png'), unsafe_allow_html=True)

if __name__ == '__main__':
    main()

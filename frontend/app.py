import streamlit as st
import requests
import base64


st.header('Project Yoda ')

# File upload function:

test_image = st.file_uploader(label="Choose a file", type=['jpg','png'])

if test_image != None:
    st.image(test_image)
    test_image_bytes = base64.b64encode(test_image.read()) # encoding the image to base64
    post_object = {'image': test_image_bytes} # creating post object


# Post request to prediction api

if st.button('Classify me!'):
    st.balloons()
    st.write(post_object)
    result = requests.get('https://projectyoda-zl47dkr23a-ew.a.run.app/predict', data=post_object)
    result = result.json()
    st.write(result)
    st.write(result['prediction'])

if st.button('Check API'):
    st.balloons()
    test_result = requests.get('https://projectyoda-zl47dkr23a-ew.a.run.app/')
    st.write(test_result)

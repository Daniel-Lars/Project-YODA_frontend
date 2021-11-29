from google.cloud import storage

import streamlit as st
import requests

BUCKET_NAME = 'wagon-data-745-project-yoda'
DESTINATION_BLOB_NAME = 'images/image.jpg'


def upload_blob(file):
    """Uploads a file to the bucket."""

    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(DESTINATION_BLOB_NAME)

    blob.upload_from_file(file)

st.header('Project Yoda ')

# File upload function:

test_image = st.file_uploader(label="Choose a file", type=['jpg','png'])

if test_image != None:
    st.image(test_image)
    upload_blob(test_image)


# Post request to prediction api

if st.button('Classify me!'):
    st.balloons()
    result = requests.get('https://projectyoda-zl47dkr23a-ew.a.run.app/predict')
    result = result.json()
    st.write(result['prediction'])

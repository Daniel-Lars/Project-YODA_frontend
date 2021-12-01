from google.cloud import storage
from PIL import Image
from random import choice
from time import sleep
import requests
import streamlit as st

BUCKET_NAME = 'wagon-data-745-project-yoda'
DESTINATION_BLOB_NAME = 'images/image.jpg'
URL_PROD = 'https://projectyoda-zl47dkr23a-ew.a.run.app/predict'
URL_DEV = 'http://34.140.153.26:5000/predict'

url = URL_PROD


# helper functions:

## upload image to gcp
def upload_blob(file):
    """Uploads a file to the bucket."""

    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(DESTINATION_BLOB_NAME)

    blob.upload_from_file(file)

st.header('Project Yoda ')

## show Yoda with wise comments
def show_yoda(col1, col2):
    quotes = [
        'When you look at the dark side, careful you must be. For the dark side looks back.',
        'If no mistake you have made, losing you are. A different game you should play.',
        'You must unlearn what you have learned.',
        'Size matters not. Look at me. Judge me by my size, do you?',
        'Try not. Do. Or do not. There is no try.',
        'Train yourself to let go of everything you are afraid to lose.',
        'Named must your fear be before banish it you can.'
    ]

    yoda = Image.open('./yoda.png')
    col1.image(yoda, width=128)

    text1 = 'Hmm.. the Force I must use to predict your image..'
    col2.write(text1)
    sleep(2)
    col2.write('Some wisdom I will share in the meantime:')
    sleep(2)
    wisdom = choice(quotes)
    col2.write(wisdom)

## make prediction
def make_prediction(col2):
    result = requests.get(url)
    result = result.json()
    prediction = result['prediction']

    if prediction == None:
        pass
    if prediction == 'YODA':
        prediction = 'ME'
    if prediction == 'DARTH VADER':
        prediction = 'my old enemy DARTH VADER'
    col2.markdown(f'Hmm.. yes.. **{prediction}** this is!')


# for frontend rendering:

## get image from user input
test_image = st.file_uploader(label="Choose a file", type=['jpg','png'])

if test_image != None:
    st.image(test_image, width=256)
    upload_blob(test_image)


## on button click, make GET request to prediction api
if st.button('Classify me!'):

    col1, col2 = st.columns((1,3))

    show_yoda(col1, col2)

    try:
        make_prediction(col2)
    except:
        st.write('Not able to get prediction..')

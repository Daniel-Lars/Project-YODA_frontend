import streamlit as st
import requests

st.header('Project Yoda ')

uploaded_file = st.file_uploader("Choose a file")

url = 'https://projectyoda-oikr5k2fcq-ew.a.run.app/'

response = requests.get(url).json()


def classification():
    button = st.button(label='Classify me!')
    return button


if uploaded_file is not None:
    st.image(uploaded_file)
    classification()

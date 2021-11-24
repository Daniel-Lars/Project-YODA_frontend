import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
import time

st.title('Lego Prediction')
st.write('Upload your image')
dataset_name = st.sidebar.selectbox(
    "Lego Set", ("Harry Potter", "Jurassic World", "Marvel", "Star Wars"))
uploaded_file = st.file_uploader("Choose a file")
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete+1)

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.image(bytes_data)
# To convert to a string based IO:
stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
st.image(stringio)

# To read file as string:
string_data = stringio.read()
st.image(string_data)
# Can be used wherever a "file-like" object is accepted:
dataframe = pd.read_csv(uploaded_file)
st.image(dataframe)

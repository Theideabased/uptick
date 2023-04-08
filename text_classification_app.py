import streamlit as st
import panda as pd
import numpy as np

@st_cache.data
st.text_input(label="Text", placeholder="write your text")
st.write(f'{Text} is a nice one')

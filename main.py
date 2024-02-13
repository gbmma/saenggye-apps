import streamlit as st  
from streamlit.components.v1 import html 

import os
import json

import openai

path = os.path.dirname(__file__)

# Load translations from JSON file
with open(path+"/../main/translations.json") as f:
    transl = json.load(f) 
 
st.set_page_config(
    page_title="경기북부병무지청 생계심사 자가진단",
    page_icon=":pickup_truck:",
    initial_sidebar_state="expanded",
)

st.write("# 경기북부병무지청 생계 자가진단")
 

st.markdown(
    """##### 테스트중!

"""
)  

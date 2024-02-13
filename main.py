import streamlit as st



st.set_page_config(
    page_title="경기북부병무지청 생계심사 자가진단",
    page_icon=":pickup_truck:",
    initial_sidebar_state="expanded",
)

st.write("# 경기북부병무지청 생계 자가진단")

st.sidebar.success("여긴")

st.markdown(
    """##### 테스트중!

"""
)

import streamlit as st
from streamlit.components.v1 import html
from streamlit_extras.buy_me_a_coffee import button
import os

# Trick to preserve the state of your widgets across pages
for k, v in st.session_state.items():
    st.session_state[k] = v
##

st.set_page_config(
    page_title="About",
    page_icon="📰",
    layout="wide"
)

# Works with streamlit==1.17.0
# TODO: Review class names for future versions
st.markdown("""
  <style>
      ul[class="css-j7qwjs e1fqkh3o7"]{
        position: relative;
        padding-top: 2rem;
        display: flex;
        justify-content: center;
        flex-direction: column;
        align-items: center;
      }
      .css-17lntkn {
        font-weight: bold;
        font-size: 18px;
        color: grey;
      }
      .css-pkbazv {
        font-weight: bold;
        font-size: 18px;
      }
  </style>""", unsafe_allow_html=True)

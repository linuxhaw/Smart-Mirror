import requests
import streamlit as st
from streamlit_lottie import st_lottie
import os 
st.set_page_config(
    page_title="Smart Mirror",
    page_icon=":tada:",
    layout="wide")

st.title("Smart-Mirror AI :mirror:")
st.subheader("Female Outfit Recommendation CV Project :dress:")


# # Display the button using markdown
# st.markdown(button_html, unsafe_allow_html=True)

if st.button("Try Now"):
    st.write('<meta http-equiv="refresh" content="0; URL=http://localhost:8501/main">', unsafe_allow_html=True)

hide_sidebar_style = """
    <style>
        [data-testid="stSidebar"] {
            display: none;  /* Hide the sidebar */
        }
        [data-testid="stSidebarNav"] {
            display: none;  /* Hide the sidebar navigation */
        }
        .css-qrbaxs {
            margin-left: 0rem;  /* Adjust the main content margin */
        }
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

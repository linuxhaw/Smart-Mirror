import requests
import streamlit as st
from streamlit_lottie import st_lottie
import os 
st.set_page_config(
    page_title="Smart Mirror",
    page_icon=":tada:",
    layout="wide")

st.title("Smart-Mirror AI :mirror:")
st.title("Outfit Recommendation CV")

# st.page_link("./pages/main.py", label="Start", icon="1️⃣")

# st.link_button("Get Started", "http://localhost:8501/main")


button_html = """
    <a href="/main">
        <button style="
            background-color: #007BFF;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 16px 2px;
            cursor: pointer;
            border-radius: 8px;
        ">Get Started</button>
    </a>
"""

# Display the button using markdown
st.markdown(button_html, unsafe_allow_html=True)

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

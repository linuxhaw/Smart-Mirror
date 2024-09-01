import requests
import streamlit as st
from streamlit_lottie import st_lottie
import os 
st.set_page_config(
    page_title="Smart Mirror",
    page_icon=":tada:",
    layout="wide",
    initial_sidebar_state="collapsed"
)
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Smart-Mirror AI :mirror:")
st.subheader("Female Outfit Recommendation CV Project")
# st.code ("To create a smart mirror that provides personalized outfit recommendations to women based on their preferences and purposes.")
st.markdown("To create a smart mirror that provides personalized outfit recommendations to women based on their preferences and purposes.:sparkles:")


if st.button("Try Beta Version"):
    st.write('<meta http-equiv="refresh" content="0; URL=http://localhost:8501/main">', unsafe_allow_html=True)

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
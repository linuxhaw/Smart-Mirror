import streamlit as st
from final_function import recommender
from pages.main import user_selection

# Set page configuration
st.set_page_config(page_title="Results - Outfit Recommendation", page_icon=":tada:", layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Check if the session state contains the required data
if "selected_age" in st.session_state and st.session_state["selected_age"] is not None:
    # Retrieve stored data from session state
    selected_age = st.session_state["selected_age"]
    selected_event = st.session_state["selected_event"]
    selected_style = st.session_state["selected_style"]
    user_selection = st.session_state["user_selection"]

    # Display the selected age and event
    st.title("AI Recommended Outfits")
    st.subheader(f"This outfit is suitable for {selected_event} between age {selected_age}")

    def display_result_images(path):
        # Display the image at the given path
        st.image(path)

    # Call the recommender function and get the paths and descriptions
    recommender_output = recommender(user_selection, selected_age, selected_event, selected_style)

    # Check the type and length of output from recommender
    if isinstance(recommender_output, tuple) and len(recommender_output) == 2:
        image_paths, descriptions = recommender_output

        # Display each image with its description
        for path, description in zip(image_paths, descriptions):
            display_result_images(path)
            st.write(description)  # Display the description if needed
    else:
        st.error("Error in recommender function output: Expected a tuple of two lists.")

# Button to go back to the main page
if st.button("Back to Selection"):
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
import streamlit as st
from final_function import recommender
from rembg import remove
from PIL import Image
import io

# Set page configuration
st.set_page_config(
    page_title="Smart Mirror",
    page_icon=":tada:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load and apply custom CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

@st.cache_data  # Cache image processing to speed up reloading
def process_image(path):
    with open(path, "rb") as image_file:
        image = Image.open(image_file).convert("RGBA")
        # Resize the image to speed up processing
        image.thumbnail((800, 800))  # Adjust size as needed
        # Remove background
        image_no_bg = remove(image)
        return image_no_bg

# Check if the session state contains the required data
if "selected_age" in st.session_state and st.session_state["selected_age"] is not None:
    # Retrieve stored data from session state
    selected_age = st.session_state["selected_age"]
    selected_event = st.session_state["selected_event"]
    selected_style = st.session_state["selected_style"]
    user_selection = st.session_state["user_selection"]

    # Display the selected age and event
    st.title("AI Generated Recommend Outfits :magic_wand: :sparkles:")
    st.subheader(f"This outfit is suitable for {selected_event} between age {selected_age}.")

    def display_result_images(path):
        # Process image and display
        image_no_bg = process_image(path)
        st.image(image_no_bg)

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

# Hide sidebar control (not applicable for this script as sidebar is collapsed by default)
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none;
    }
</style>
""",
    unsafe_allow_html=True,
)
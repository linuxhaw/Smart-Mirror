import streamlit as st

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
    st.title("Recommended Outfits")
    st.write(f"### Age Range: {selected_age}")
    st.write(f"### Event: {selected_event}")
    st.write(f"### Style: {selected_style}")

    # Function to display selected images in a grid format
    def display_selected_images(category, images):
        st.write(f"### {category}")
        cols = st.columns(6)
        for idx, image in enumerate(images):
            with cols[idx % 6]:  # Distribute images across columns
                st.image(image, use_column_width=True)  # Display image

    # Display selected images for each category
    for category, images in user_selection.items():
        if images:  # Only display if there are selected images
            display_selected_images(category, images)

else:
    st.write("No data available. Please go back to the selection page.")

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
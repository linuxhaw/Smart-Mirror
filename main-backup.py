import requests
import streamlit as st
from streamlit_lottie import st_lottie
import os 
st.set_page_config(
    page_title="Smart Mirror",
    page_icon=":tada:",
    layout="wide")

with open ('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



# Primary accent for interactive elements
primaryColor = '#FFA4EB'

# Background color for the main content area
backgroundColor = '#273346'

# Background color for sidebar and most interactive widgets
secondaryBackgroundColor = '#FFA4EB'

# Color used for almost all text
textColor = '#FFFFFF'

# Font family for all text in the app, except code blocks
# Accepted values (serif | sans serif | monospace) 
# Default: "sans serif"
font = "sans serif"

st.title("Smart-Mirror AI :mirror:")
st.title("Outfit Recommendation CV")

age = st.select_slider(
    "Select your age",
    options=[
        "14-25",
        "26-35",
        "36-44",
    ],
)

# Define age ranges and events

events = ["Wedding/Party", "Office/Business", "Casual/Day Out", "Date Night/Evening Out", "Shopping/Hanging Out"]


# Age Range and Event Selection

selected_event = st.selectbox("Select Event:", events)


# Define paths to your image folders
base_path = "./Dataset"  # Adjust this path to your base image directory

# Define the categories with actual image paths
categories = {
    "Tops": [os.path.join(base_path, "top", f"top{i}.jpg") for i in range(1, 13)], 
    "Blouses": [os.path.join(base_path, "blouse", f"blouse{-i}.jpg") for i in range(1, 13)],
    "Cardigan": [os.path.join(base_path, "cardigan", f"cardigan{-i}.jpg") for i in range(1, 13)],
    "Dresses": [os.path.join(base_path, "dress", f"dress{-i}.jpg") for i in range(1, 13)],
    "Jackets": [os.path.join(base_path, "jacket", f"jacket{-i}.jpg") for i in range(1, 13)],
    "Shirts": [os.path.join(base_path, "Shirt", f"shirt{-i}.jpg") for i in range(1, 13)],
    "Skirts": [os.path.join(base_path, "short skirt", f"short-skirt{-i}.jpg") for i in range(1, 13)],
    "Pants": [os.path.join(base_path, "style pants", f"style-pants{-i}.jpg") for i in range(1, 13)],
    "Heels": [os.path.join(base_path, "heels", f"heels{-i}.jpg") for i in range(1, 13)],
    "Sneakers": [os.path.join(base_path, "sneakers", f"sneakers{-i}.jpg") for i in range(1, 13)],
    "Slippers": [os.path.join(base_path, "slippers", f"slippers{-i}.jpg") for i in range(1, 13)],
}


# User Selection Storage
user_selection = {}

# Function to display images in a grid format
def display_image_grid(category, images):
    st.write(f"### {category}")
    cols = st.columns(6)
    selected_images = []
    for idx, image in enumerate(images):
        with cols[idx % 6]:  # Distribute images across columns
            selected = st.checkbox(f"Select", key=f"{category}_{idx}_{image}")
            st.image(image, use_column_width=True)  # Display image
            if selected:
                selected_images.append(image)
    return selected_images

# Display each category with images in a grid format
for category, images in categories.items():
    user_selection[category] = display_image_grid(category, images)


if st.button("Generate Recommend Outfit"):
    # Here, you would add the AI recommendation logic
    st.write("Processing your outfit recommendations...")
    st.write(f"Selected Age: {age}, Selected Event: {selected_event}")
    st.write(f"Your Selections: {user_selection}")

if st.button("Reset",type="primary") :
    # Refresh the page by rerunning the script
    st.experimental_rerun()

st.sidebar.header("Female Outfits")
st.sidebar.markdown('<a href="#tops" style="text-decoration: none; color: inherit;">Tops</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#blouses" style="text-decoration: none; color: inherit;">Blouses</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#cardigan" style="text-decoration: none; color: inherit;">Cardigan</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#dresses" style="text-decoration: none; color: inherit;">Dresses</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#jackets" style="text-decoration: none; color: inherit;">Jackets</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#shirts" style="text-decoration: none; color: inherit;">Shirts</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#skirts" style="text-decoration: none; color: inherit;">Skirts</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#pants" style="text-decoration: none; color: inherit;">Pants</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#heels" style="text-decoration: none; color: inherit;">Heels</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#sneakers" style="text-decoration: none; color: inherit;">Sneakers</a>', unsafe_allow_html=True)
st.sidebar.markdown('<a href="#slippers" style="text-decoration: none; color: inherit;">Slippers</a>', unsafe_allow_html=True)
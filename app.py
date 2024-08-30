import requests
import streamlit as st
from streamlit_lottie import st_lottie
import os 


st.set_page_config(page_title="Smart Mirror",page_icon=":tada:",layout="wide")

st.title("Smart-Mirror AI :mirror:")
st.title("Outfit Recommendation CV")
age = st.select_slider(
    "Select your age",
    options=[
        "13-19",
        "20-35",
        "36-50",
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
    "Shirts": [os.path.join(base_path, "Shirt", f"shirt{-i}.jpg") for i in range(1, 13)],
    "Skirts": [os.path.join(base_path, "short skirt", f"short-skirt{-i}.jpg") for i in range(1, 13)],
    "Pants": [os.path.join(base_path, "style pants", f"style-pants{-i}.jpg") for i in range(1, 13)],
    "Heels": [os.path.join(base_path, "heels", f"heels{-i}.jpg") for i in range(1, 13)],
    "Sneakers": [os.path.join(base_path, "sneakers", f"sneakers{-i}.jpg") for i in range(1, 13)]
}


# User Selection Storage
user_selection = {}

# Function to display images in a grid format
def display_image_grid(category, images):
    st.write(f"### {category}")
    cols = st.columns(3)
    selected_images = []
    for idx, image in enumerate(images):
        with cols[idx % 3]:  # Distribute images across columns
            selected = st.checkbox(f"Select", key=f"{category}_{idx}_{image}")
            st.image(image, use_column_width=True)  # Display image
            if selected:
                selected_images.append(image)
    return selected_images

# Display each category with images in a grid format
for category, images in categories.items():
    user_selection[category] = display_image_grid(category, images)

# Submit Button to get outfit recommendation
if st.button("Recommend Outfit"):
    # Here, you would add the AI recommendation logic
    st.write("Processing your outfit recommendations...")
    st.write(f"Selected Age: {age}, Selected Event: {selected_event}")
    st.write(f"Your Selections: {user_selection}")

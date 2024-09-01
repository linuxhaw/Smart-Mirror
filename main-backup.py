import streamlit as st
import os

st.set_page_config(
    page_title="Smart Mirror",
    page_icon=":tada:",
    layout="wide"
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Initialize session state if not already initialized
if 'selected_age' not in st.session_state:
    st.session_state['selected_age'] = None
if 'selected_event' not in st.session_state:
    st.session_state['selected_event'] = None
if 'user_selection' not in st.session_state:
    st.session_state['user_selection'] = {}

# Age selection
age = st.select_slider(
    "Select your age",
    options=["14-25", "26-35", "36-44"]
)

# Event selection
events = ["Wedding/Party", "Office/Business", "Casual/Day Out", "Date Night/Evening Out", "Shopping/Hanging Out"]
selected_event = st.selectbox("Select Event:", events)

# Style selection
style = ["Top and Skirt", "Dress", "Shirt and pants", "Blouse and skirt", "Cardigan and pants" ,"Jacket and pants"]
selected_style = st.multiselect("Select Style:", style)

# Define paths to your image folders
base_path = "./Dataset"  # Adjust this path to your base image directory

# Define the categories with actual image paths
categories = {
    "Tops": [os.path.join(base_path, "top", f"top{-i}.jpg") for i in range(1, 13)], 
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

# Store data in session state and navigate to the results page when the button is clicked
if st.button("Generate Recommend Outfit"):
    # Store selected data in session state
    st.session_state["selected_age"] = age
    st.session_state["selected_event"] = selected_event
    st.session_state["selected_style"] = selected_style
    st.session_state["user_selection"] = user_selection


    # st.write("Processing your outfit recommendations...")
    # st.write(f"Selected Age: {age}, Selected Event: {selected_event}, Selected Style: {selected_style}")
    # st.write(f"Your Selections: {user_selection}")
    # Redirect to results page
    # st.write('<meta http-equiv="refresh" content="0; URL=http://localhost:8501/result">', unsafe_allow_html=True)

    st.text("Its processing,please wait and click okay.")
    st.page_link("pages/result.py",label="Okay")



# Sidebar
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
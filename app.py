import streamlit as st
import app1  # Import App 1 (Image Generation)

def welcome_page():
    st.title("Welcome to AI-Powered Tools")
    st.markdown("""
    ### Explore the world of AI
    Our application offers the following tools:
    - *🔹 Image Generation*: Use AI to create images based on your imagination.
    .

    Get started by navigating to the tools from the sidebar.
    """)
    st.image("welcome_image.jpg", use_column_width=True, caption="AI-Powered Creativity")  # Add a relevant image

# Navigation between pages
st.sidebar.title("MENU")
page = st.sidebar.radio("Go to", ["Home", "Image Generation"])

if page == "Welcome":
    welcome_page()
elif page == "Image Generation":
    app1.run()  # Call the run function from app1.py
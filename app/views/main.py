import streamlit as st

# Set the page title
st.set_page_config(
    page_title="Main Page",
    layout="wide"
)

# Display a title
st.title("Hello, World!")

# Display some text
st.write("Welcome to your first Streamlit app!")

with st.sidebar:
    st.write("### Sidebar")
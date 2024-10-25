import streamlit as st

from app.services.house import get_pyg_renderer

# Set the page title
st.set_page_config(
    page_title="Explore Data",
    layout="wide"
)

renderer = get_pyg_renderer()

renderer.explorer()
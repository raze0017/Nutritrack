import streamlit as st

st.set_page_config(
    page_title="NutriTrack",
    page_icon="👋",
)

st.write("# Welcome to NutriTrack! 👋")

st.sidebar.success("Select a recommendation app.")

st.markdown(
    """
    A diet recommendation web application using content-based approach with Scikit-Learn, FastAPI and Streamlit.
    """
)
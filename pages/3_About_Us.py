import streamlit as st
from utility import check_password
from dotenv import load_dotenv
import os

if not check_password():
    st.stop()  # Do not continue if check_password is not True.

st.title("About Us")
st.caption("🚀 An AI Champions Bootcamp Project")
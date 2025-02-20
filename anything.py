#streamlit app
import streamlit as st
st.write("hey")
st.sidebar.write("sidebar")
if st.button("coffee"):
  st.write("Let's make coffee")

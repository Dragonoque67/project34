#streamlit app
import streamlit as st
st.write("hey")
st.sidebar.write("sidebar")
options= st.selectbox(["coffee","juice","tea"]):
if options=="coffee":
  st.write("Let's make coffee")
  milk=st.number_input("percentage of milk :",value=60)
  st.info(f"milk amount is {milk}")

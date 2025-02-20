#streamlit app
import streamlit as st
st.write("hey")
st.sidebar.write("sidebar")
options= st.selectbox("options",["coffee","juice","tea"])
if options=="coffee":
  st.write("Let's make coffee")
  milk=st.number_input("percentage of milk :",value=60,min_value=0,max_value=100,step=5)
  st.info(f"milk amount is {milk}")
elif options

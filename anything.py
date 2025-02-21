#streamlit app
import streamlit as st
st.write("hey little gayboi")
image_local = Image.open("yoyo")
st.image(image_local, caption="Local Image", use_column_width=True)
st.button('fruity')
st.checkbox('are you gay?')
st.slider("how much u gay?",0,100)
if st.button("garv's gay pics"):
    st.write("go away rajat")

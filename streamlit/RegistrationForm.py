import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title="Student Registration form", page_icon="🎓" , layout="centered" )

st.divider()
st.title("Student Profile Registration 🎓")
st.divider()

student_photo = st.file_uploader("Upload Student Photo", type=["jpg", "jpeg", "png"])
name = st.text_input("Student Name : ")
father = st.text_input("Father's Name : ")
college = st.text_input("College Name : ")
email = st.text_input("Email : ")
mobile = st.text_input("Mobile number : ")
skills = st.multiselect("Skills : " , ["Python" , "Java", "C++", "Data Science", "Web Development"])

st.button("Register")

# Show
st.divider()
st.markdown(
    "<h1 style='text-align: center;'>Student Profile</h1>",
    unsafe_allow_html=True
)
st.divider()
if student_photo is not None:
    st.image(student_photo, caption="Student Photo", width=200)
st.write("**Name                :** ", name)
st.write("**Father's Name       :** ",father)
st.write("**College Name        :** ",college)
st.write("**Email               :** ",email)
st.write(f"**Mobile number       :** {mobile}")
st.write(f"**Skills              :** \n" , skills)





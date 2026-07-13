import streamlit as st

st.set_page_config(page_title="Student Registration form", page_icon="🎓" , layout="wide" )
st.title("Student Registration Form")

name = st.text_input("Student Name")
father = st.text_input("Father's Name")
email = st.text_input("Email")
mobile = st.text_input("Mobile number")
gender = st.radio("Gender:" , ["MALE" , "FEMALE", "OTHER"])
age = st.number_input("Age:",min_value=18,max_value=50,step=1)
course = st.selectbox("Course:" ,["Btech" , "MTECH" , "PHD" , "BCA" , "MCA" , "BBA" , "MBA"])
branch = st.selectbox("Branch" ,["CSE" , "IT" , "ECE" , "ME" , "CE"])
semester = st.selectbox("Semester " , ["CSE" , "IT" , "ECE" , "ME" , "CE"] )
address = st.text_area("Adress:")
agree = st.checkbox("I Agree to terms and condition")

if st.button("Register"):
    if name == " " or email ==  " "  or address == " ":
        st.error("Please fill in all required feilds")
    elif not agree:
        st.warning("Please agree to terms and conditino")
    else:
        st.success("Student Registration Successfull")
    
        st.header("Student details")
        st.write("**Name:** ", name)
        st.write("**Father's Name:** ",father)
        st.write("**Email:** ",email)
        st.write(f"**Mobile number :** {mobile}")
        st.write(f"**Gender :** {gender}")
        st.write(f"**Age :** {age}")
        st.write(f"**Course :** {course}")
        st.write(f"**Branch :** {branch}")
        st.write(f"**Semester :** {semester}")
        st.write(f"**Address :** {address}")
        st.balloons()
        
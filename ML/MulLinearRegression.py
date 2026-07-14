import pandas as pd
import sklearn.linear_model as lm
import streamlit as st

df = pd.DataFrame({})
df = pd.read_csv("multiple_linear_salary_dataset_50_records.csv")

X= df[["Experience" , "Education_Level" , "Age"]]
Y = df["Salary"]

model = lm.LinearRegression()
model.fit(X,Y)

st.set_page_config(
    page_title="ML Model Testing",
    page_icon="@",
    layout="centered"
)

st.title("ML Model Testing")
exp = st.number_input("Experience : ")
ed= st.slider("Education Level : ",10,20,15)
age = st.number_input("Age : ", min_value = 18)

if st.button("Predict"):
    st.title("Salary Prediction ")
    predict = model.predict([[exp,ed,age]])
    st.write(f"**Prediction :**     {predict}")


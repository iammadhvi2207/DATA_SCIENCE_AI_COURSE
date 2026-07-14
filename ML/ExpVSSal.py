import pandas as pd
import sklearn.linear_model as lm
import streamlit as st

st.set_page_config(
    page_title="Salary Prediction System 💵",
    page_icon="@",
    layout="wide"
    )

st.title("Salary Prediction System 💵")
st.divider()

df = pd.DataFrame({})
df = pd.read_csv("experience_salary_40_records.csv")

X = df[['Experience']]
Y = df['Salary']

model = lm.LinearRegression()
model.fit(X,Y)

exp = st.slider("Experience" ,0,90,20)

if st.button("Predict"):            # Now this works only when the button is tapped
    predict_sal = model.predict([[exp]])
    st.write(f"**Prediction:** ₹{predict_sal[0]:,.2f}")
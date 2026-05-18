import streamlit as st
import pickle
import pandas as pd

# Load saved files
model = pickle.load(open("churn_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.title("Customer Churn Prediction")
st.write("Predict whether customer will churn")

# -------- User Inputs --------

gender = st.selectbox("Gender", ["Male","Female"])

senior = st.selectbox("Senior Citizen",[0,1])

partner = st.selectbox("Partner",["Yes","No"])

dependents = st.selectbox("Dependents",["Yes","No"])

tenure = st.slider("Tenure (months)",0,72,12)

monthly = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    max_value=200.0,
    value=70.0
)

total = st.number_input(
    "Total Charges",
    min_value=0.0,
    max_value=10000.0,
    value=1000.0
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month","One year","Two year"]
)

internet = st.selectbox(
    "Internet Service",
    ["DSL","Fiber optic","No"]
)

payment = st.selectbox(
    "Payment Method",
[
"Electronic check",
"Mailed check",
"Bank transfer (automatic)",
"Credit card (automatic)"
]
)

# -------- Build data --------

input_data=dict.fromkeys(columns,0)

# numeric
if 'tenure' in input_data:
    input_data['tenure']=tenure

if 'MonthlyCharges' in input_data:
    input_data['MonthlyCharges']=monthly

if 'TotalCharges' in input_data:
    input_data['TotalCharges']=total

if 'SeniorCitizen' in input_data:
    input_data['SeniorCitizen']=senior


# one hot columns

col='gender_'+gender
if col in input_data:
    input_data[col]=1

col='Partner_'+partner
if col in input_data:
    input_data[col]=1

col='Dependents_'+dependents
if col in input_data:
    input_data[col]=1

col='Contract_'+contract
if col in input_data:
    input_data[col]=1

col='InternetService_'+internet
if col in input_data:
    input_data[col]=1

col='PaymentMethod_'+payment
if col in input_data:
    input_data[col]=1


final_df=pd.DataFrame([input_data])

final_scaled=scaler.transform(final_df)

# -------- Prediction --------

if st.button("Predict"):

    prediction=model.predict(final_scaled)

    probability=model.predict_proba(
        final_scaled
    )

    st.write(
    "Churn Probability:",
    round(probability[0][1]*100,2),
    "%"
    )

    if prediction[0]==1:
        st.error(
        "Customer likely to Churn"
        )

    else:
        st.success(
        "Customer likely to Stay"
        )
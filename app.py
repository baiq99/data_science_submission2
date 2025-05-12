import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load trained model and preprocessing assets
model = joblib.load('./model/final_rdf_model.joblib')
scaler = joblib.load('./model/scaler.pkl')
encoded_columns = joblib.load('./model/encoded_feature_names.pkl')
selected_features = joblib.load('./model/selected_feature_names.pkl')

# Streamlit UI
st.title('Student Dropout Prediction')

# Input fields
curricular_units_2nd_sem_approved = st.number_input('Curricular Units 2nd Semester Approved', min_value=0, max_value=30, value=15)
curricular_units_2nd_sem_grade = st.number_input('Curricular Units 2nd Semester Grade', min_value=0, max_value=20, value=15)
curricular_units_1st_sem_approved = st.number_input('Curricular Units 1st Semester Approved', min_value=0, max_value=30, value=15)
curricular_units_1st_sem_grade = st.number_input('Curricular Units 1st Semester Grade', min_value=0, max_value=20, value=15)
tuition_fees_up_to_date = st.selectbox('Tuition Fees Up to Date', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
scholarship_holder = st.selectbox('Scholarship Holder', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
curricular_units_2nd_sem_enrolled = st.number_input('Curricular Units 2nd Semester Enrolled', min_value=0, max_value=30, value=20)
curricular_units_1st_sem_enrolled = st.number_input('Curricular Units 1st Semester Enrolled', min_value=0, max_value=30, value=20)
admission_grade = st.slider('Admission Grade', min_value=0.0, max_value=200.0, value=5.0, step=0.1)
displaced = st.selectbox('Displaced', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')

# Raw input as dictionary
user_input_dict = {
    'Curricular Units 2nd Semester Approved': curricular_units_2nd_sem_approved,
    'Curricular Units 2nd Semester Grade': curricular_units_2nd_sem_grade,
    'Curricular Units 1st Semester Approved': curricular_units_1st_sem_approved,
    'Curricular Units 1st Semester Grade': curricular_units_1st_sem_grade,
    'Tuition Fees Up to Date': tuition_fees_up_to_date,
    'Scholarship Holder': scholarship_holder,
    'Curricular Units 2nd Semester Enrolled': curricular_units_2nd_sem_enrolled,
    'Curricular Units 1st Semester Enrolled': curricular_units_1st_sem_enrolled,
    'Admission Grade': admission_grade,
    'Displaced': displaced
}

# Convert to DataFrame with one row
input_df = pd.DataFrame([user_input_dict])

# One-hot encode to match training format
input_encoded = pd.get_dummies(input_df)

# Reindex to match training encoded feature order
input_encoded = input_encoded.reindex(columns=encoded_columns, fill_value=0)

# Standardize all numerical features
input_scaled = scaler.transform(input_encoded)

# Convert to DataFrame so we can select features
input_scaled_df = pd.DataFrame(input_scaled, columns=encoded_columns)

# Select only the top 20 features
input_final = input_scaled_df[selected_features]

# Predict using model
if st.button('Predict'):
    prediction = model.predict(input_final)[0]

    status_dict = {
        0: 'Dropout',
        1: 'Enrolled',
        2: 'Graduate'
    }

    st.success(f"The model predicts that the student is likely to be: **{status_dict[prediction]}**")

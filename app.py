import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("thyroid_recurrence_model.pkl")

# Title
st.title(" Thyroid Cancer Recurrence Prediction")
st.write("Enter the patient details below to predict thyroid cancer recurrence.")

# Inputs
age = st.number_input("Age", min_value=10, max_value=100, value=30)

gender = st.selectbox("Gender", ["F", "M"])
smoking = st.selectbox("Smoking", ["No", "Yes"])
hx_smoking = st.selectbox("History of Smoking", ["No", "Yes"])
hx_radiotherapy = st.selectbox("History of Radiotherapy", ["No", "Yes"])

thyroid_function = st.selectbox(
    "Thyroid Function",
    [
        "Clinical Hyperthyroidism",
        "Clinical Hypothyroidism",
        "Euthyroid",
        "Subclinical Hyperthyroidism",
        "Subclinical Hypothyroidism"
    ]
)

physical_exam = st.selectbox(
    "Physical Examination",
    [
        "Diffuse goiter",
        "Multinodular goiter",
        "Normal",
        "Single nodular goiter-left",
        "Single nodular goiter-right"
    ]
)

adenopathy = st.selectbox(
    "Adenopathy",
    [
        "Bilateral",
        "Extensive",
        "Left",
        "No",
        "Posterior",
        "Right"
    ]
)

pathology = st.selectbox(
    "Pathology",
    [
        "Follicular",
        "Hurthel cell",
        "Micropapillary",
        "Papillary"
    ]
)

focality = st.selectbox(
    "Focality",
    [
        "Multi-Focal",
        "Uni-Focal"
    ]
)

risk = st.selectbox(
    "Risk",
    [
        "High",
        "Intermediate",
        "Low"
    ]
)

t_stage = st.selectbox(
    "Tumor Classification (T)",
    ["T1a", "T1b", "T2", "T3a", "T3b", "T4a", "T4b"]
)

n_stage = st.selectbox(
    "Nodal Classification (N)",
    ["N0", "N1a", "N1b"]
)

m_stage = st.selectbox(
    "Metastasis Classification (M)",
    ["M0", "M1"]
)

stage = st.selectbox(
    "Cancer Stage",
    ["I", "II", "III", "IVA", "IVB"]
)

response = st.selectbox(
    "Treatment Response",
    [
        "Biochemical Incomplete",
        "Excellent",
        "Indeterminate",
        "Structural Incomplete"
    ]
)

# Encoding dictionaries
gender_map = {'F': 0, 'M': 1}
yes_no_map = {'No': 0, 'Yes': 1}

thyroid_map = {
    'Clinical Hyperthyroidism': 0,
    'Clinical Hypothyroidism': 1,
    'Euthyroid': 2,
    'Subclinical Hyperthyroidism': 3,
    'Subclinical Hypothyroidism': 4
}

physical_map = {
    'Diffuse goiter': 0,
    'Multinodular goiter': 1,
    'Normal': 2,
    'Single nodular goiter-left': 3,
    'Single nodular goiter-right': 4
}

adenopathy_map = {
    'Bilateral': 0,
    'Extensive': 1,
    'Left': 2,
    'No': 3,
    'Posterior': 4,
    'Right': 5
}

pathology_map = {
    'Follicular': 0,
    'Hurthel cell': 1,
    'Micropapillary': 2,
    'Papillary': 3
}

focality_map = {
    'Multi-Focal': 0,
    'Uni-Focal': 1
}

risk_map = {
    'High': 0,
    'Intermediate': 1,
    'Low': 2
}

t_map = {
    'T1a': 0,
    'T1b': 1,
    'T2': 2,
    'T3a': 3,
    'T3b': 4,
    'T4a': 5,
    'T4b': 6
}

n_map = {
    'N0': 0,
    'N1a': 1,
    'N1b': 2
}

m_map = {
    'M0': 0,
    'M1': 1
}

stage_map = {
    'I': 0,
    'II': 1,
    'III': 2,
    'IVA': 3,
    'IVB': 4
}

response_map = {
    'Biochemical Incomplete': 0,
    'Excellent': 1,
    'Indeterminate': 2,
    'Structural Incomplete': 3
}

# Prediction
if st.button("Predict Recurrence"):

    input_data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender_map[gender]],
        'Smoking': [yes_no_map[smoking]],
        'Hx Smoking': [yes_no_map[hx_smoking]],
        'Hx Radiothreapy': [yes_no_map[hx_radiotherapy]],
        'Thyroid Function': [thyroid_map[thyroid_function]],
        'Physical Examination': [physical_map[physical_exam]],
        'Adenopathy': [adenopathy_map[adenopathy]],
        'Pathology': [pathology_map[pathology]],
        'Focality': [focality_map[focality]],
        'Risk': [risk_map[risk]],
        'T': [t_map[t_stage]],
        'N': [n_map[n_stage]],
        'M': [m_map[m_stage]],
        'Stage': [stage_map[stage]],
        'Response': [response_map[response]]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Prediction: The patient is likely to experience thyroid cancer recurrence.")
    else:
        st.success("✅ Prediction: The patient is unlikely to experience thyroid cancer recurrence.")
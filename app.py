import streamlit as st
import numpy as np
import pandas as pd
import pickle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io


with open("stacking_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)


st.set_page_config(
    page_title="InsurePro",
    layout="wide"
)


st.title("InsurePro")
st.markdown("AI-based insurance premium prediction and risk assessment system")

st.markdown("---")


st.sidebar.header("Customer Details")

age = st.sidebar.slider("Age", 18, 65, 30)
height = st.sidebar.number_input("Height (cm)", 120.0, 220.0, 170.0)
weight = st.sidebar.number_input("Weight (kg)", 30.0, 150.0, 70.0)

children = st.sidebar.selectbox("Number of Children", [0,1,2,3,4,5])
sex = st.sidebar.selectbox("Gender", ["male", "female"])
smoker = st.sidebar.selectbox("Smoker", ["yes", "no"])
region = st.sidebar.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])


def create_features():
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    data = {
        'age': age,
        'bmi': bmi,
        'children': children,
        'smoker_bmi': bmi * (1 if smoker == 'yes' else 0)
    }

    if bmi < 18.5:
        bmi_cat = "underweight"
    elif bmi < 25:
        bmi_cat = "normal"
    elif bmi < 30:
        bmi_cat = "overweight"
    else:
        bmi_cat = "obese"

    if age <= 18:
        age_grp = "teen"
    elif age <= 35:
        age_grp = "young_adult"
    elif age <= 50:
        age_grp = "adult"
    else:
        age_grp = "senior"

    data.update({
        'sex': sex,
        'smoker': smoker,
        'region': region,
        'bmi_category': bmi_cat,
        'age_group': age_grp
    })

    df = pd.DataFrame([data])
    df = pd.get_dummies(df)

    for col in model_columns:
        if col not in df.columns:
            df[col] = 0

    df = df[model_columns]

    return df, bmi


def generate_pdf(prediction, bmi):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("InsurePro - Insurance Quote", styles['Title']))
    content.append(Spacer(1, 12))

    content.append(Paragraph(f"Age: {age}", styles['Normal']))
    content.append(Paragraph(f"Gender: {sex}", styles['Normal']))
    content.append(Paragraph(f"Region: {region}", styles['Normal']))
    content.append(Paragraph(f"Children: {children}", styles['Normal']))
    content.append(Paragraph(f"Smoker: {smoker}", styles['Normal']))
    content.append(Paragraph(f"BMI: {bmi:.2f}", styles['Normal']))

    content.append(Spacer(1, 12))
    content.append(Paragraph(f"Estimated Premium: $ {prediction:,.2f}", styles['Heading2']))

    doc.build(content)
    buffer.seek(0)

    return buffer


st.markdown("Prediction")

if st.button("Predict Premium"):

    input_df, bmi = create_features()
    prediction = model.predict(input_df)[0]

    st.subheader("Estimated Insurance Charges")
    st.write(f"$ {prediction:,.2f}")

    st.subheader("Computed BMI")
    st.write(f"{bmi:.2f}")

    # Generate PDF
    pdf = generate_pdf(prediction, bmi)

    st.download_button(
        label="Download Quote as PDF",
        data=pdf,
        file_name="insurance_quote.pdf",
        mime="application/pdf"
    )

st.markdown("---")
st.markdown("InsurePro | AI-driven insurance pricing system")
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Analysis App", layout="wide")

st.title("📊 Data Analysis Dashboard")

uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx", "xls"]
)

if uploaded_file is not None:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("File uploaded successfully!")

    st.subheader("Dataset Preview")
    st.dataframe(df)

    st.subheader("Dataset Information")
    st.write(df.describe())

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

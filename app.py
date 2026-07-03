import streamlit as st

st.header("Dataset Preview")
st.dataframe(df.head())

st.header("Last 5 Rows")
st.dataframe(df.tail())

st.header("Dataset Information")
st.write(df.info())

st.header("Statistical Summary")
st.dataframe(df.describe())

st.header("Missing Values")
st.dataframe(df.isnull().sum())

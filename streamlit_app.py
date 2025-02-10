import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Streamlit")
st.write("Testing")

st.sidebar.title("Select a dataset")

st.image("image.png")

df = pd.read_csv("listings.csv")

app_mode = st.sidebar.selectbox("Select a page",["01 Introduction","02 Data Visualization"])

if app_mode == "01 Introduction":
    st.markdown("## Summary")
    st.dataframe(df.head(5))

    st.dataframe(df.describe())

elif app_mode == "02 Data Visualization":
    list_of_variables = df.columns
    user_selections = st.multiselect("Select a variable",list_of_variables,["price","reviews_per_month"])
    st.markdown("## Bar chart")
    st.bar_chart(df[user_selections[0]])

    st.markdown("## Line chart")
    st.line_chart(df[user_selections[0]])

    st.markdown("## Seaborn Bar Chart")    
    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(x=user_selections[0],y=user_selections[1],data=df,palette="Blues")
    st.pyplot(fig)


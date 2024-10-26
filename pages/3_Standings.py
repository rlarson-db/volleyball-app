import streamlit as st
import pandas as pd

st.header("STANDINGS")

df_standings = pd.read_csv('static/schedule.csv')

st.dataframe(df_standings)

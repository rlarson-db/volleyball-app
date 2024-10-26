import streamlit as st
import pandas as pd

st.header("STANDINGS")

df_standings = pd.read_csv('static/schedule.csv')

st.Dataframe(df_standings)

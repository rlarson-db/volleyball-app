import streamlit as st
import pandas as pd

st.set_page_config(
   page_title="Standings",
   page_icon='948',
   layout="wide",
   initial_sidebar_state="expanded",
)

st.header("CURRENT STANDINGS")

df_standings = pd.read_csv('static/schedule.csv')

st.dataframe(df_standings,hide_index=True)

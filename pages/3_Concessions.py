import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="Concessions", page_icon=':pizza:', layout="wide")

df_concessions = pd.read_csv('static/concessions.csv')

st.header('This is the menu')

st.dataframe(df_concessions,
				height = 750,
				width = 800,
				hide_index=True)
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="Concessions", page_icon=':pizza:')

df_concessions = pd.read_csv('static/concessions.csv')

st.header('Available Concessions Options')

st.dataframe(df_concessions,
				#height = 750,
				#width = 800,
				hide_index=True)

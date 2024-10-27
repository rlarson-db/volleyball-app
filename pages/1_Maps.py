import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(
   page_title="Maps",
   page_icon='350',
   layout="wide",
   initial_sidebar_state="expanded",
)

df_locations = pd.read_csv('static/locations.csv')

with st.expander('High and Middle Schools', expanded=True):
	st.header(" High and Middle Schools")
	components.html("""<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d2191.708429147411!2d-70.25396364337496!3d43.79767358128345!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e1!3m2!1sen!2sus!4v1729814350231!5m2!1sen!2sus" width="800" height="600" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>""",height=750
				)

with st.expander('Specific Map Links', expanded=True):
    #st.write('Test')	
	st.dataframe(
		df_locations,
		height = 750,
		width = 800,
		hide_index=True,
		column_config={
		"Link": st.column_config.LinkColumn(
		"Link",
		help="Click to go to map"
						)
					}
				)
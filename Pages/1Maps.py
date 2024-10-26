import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Maps", page_icon=':world_map:', layout="wide")

#col1, col2 = st.columns(2)

#with col1:


#with col2:
st.header("Greely High and Middle Schools")
#st.header("351 Tuttle Rd, Cumberland Center, ME 04021")
components.html("""<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d2191.708429147411!2d-70.25396364337496!3d43.79767358128345!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e1!3m2!1sen!2sus!4v1729814350231!5m2!1sen!2sus" width="800" height="600" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>""",height=750
			)
    


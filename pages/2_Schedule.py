import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(
   page_title="Schedule",
   page_icon=":calendar:",
   layout="wide",
   #initial_sidebar_state="expanded",
)

# read csv
df_schedule = pd.read_csv('static/schedule.csv')

#create list of teams for sidebar selection
l_teams = []
l_teams1 = df_schedule['Team1'].unique().tolist()
l_teams2 = df_schedule['Team2'].unique().tolist()
l_teams3 = l_teams1 + l_teams2

for t in l_teams3:
    if t not in l_teams:
        l_teams.append(t)

l_teams.sort()
l_teams[0] = 'All'

#st.sidebar.header('Select team:')
#selected_team = st.sidebar.selectbox('Teams', l_teams)

with st.sidebar.form("Options"):
    st.write("Inside the form")
    selected_team = st.selectbox('Teams', l_teams)
    played_val = st.checkbox("Only Unplayed Games?")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    #if submitted:
        #st.write("Team", selected_team, "Unplayed Games Only?", played_val)

# post information
st.header('SCHEDULE')

if selected_team != 'All':
    df_filteredschedule = df_schedule[(df_schedule['Team1'] == selected_team) | (df_schedule['Team2'] == selected_team)]
else:
    df_filteredschedule = df_schedule

st.dataframe(df_filteredschedule,
				#height = 750,
				width = 800,
				hide_index=True)

# this should be removed
#st.header('PLAYOFF BRACKET')

#components.html(
#	"""<a class="maxpreps-widget-link" data-width="900" data-height="600" data-type="tournament" data-member-id="8928daf0-8ed7-452c-8944-54ab7d6e74fa" data-allow-scrollbar="true" href="https://www.maxpreps.com/tournament/view.aspx?tournamentid=97b60314-f69d-41ed-8145-e2243ace6d6b&ssid=41b23fe4-20c2-4913-877a-6e6a64958433&bracketid=aacb117d-bf3a-4ec1-ab44-83880292a4eb" >2024 MPA Volleyball Championships Class B</a><script type="text/javascript" >(function(d){var mp = d.createElement('script'),h=d.getElementsByTagName('head')[0];mp.type='text/javascript';mp.async=true;mp.src='https://www.maxpreps.com/includes/js/widget/widget.compressed.js';h.appendChild(mp);})(document);</script>"""
#	,height=900)

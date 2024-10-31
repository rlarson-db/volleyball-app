import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="Schedule",page_icon=":calendar:")

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
l_teams.insert(0,'All')

l_pools = df_schedule['Pool'].unique().tolist()
l_pools.sort()
l_pools.insert(0,'All')

l_locations = df_schedule['Location'].unique().tolist()
l_locations.sort()
l_locations.insert(0,'All')

with st.sidebar.form("Options"):
    st.write("Filtering Options:")
    selected_team = st.selectbox('Teams', l_teams)
    selected_pool = st.selectbox('Pools', l_pools)
    selected_location = st.selectbox('Location', l_locations)
    played_val = st.checkbox("Only Unplayed Games?")
    game_scores = st.checkbox("Show Individual Game Scores?")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Filter Schedule")

# post information
st.header('SCHEDULE')
st.write(f'Team: {selected_team}   |   Pool: {selected_pool}   |   Location: {selected_location}   |   Unplayed Only: {played_val}')

if selected_team != 'All':
    df_filteredschedule = df_schedule[(df_schedule['Team1'] == selected_team) | (df_schedule['Team2'] == selected_team)]
else:
    df_filteredschedule = df_schedule

if selected_pool != 'All':
    df_filteredschedule = df_filteredschedule[(df_filteredschedule['Pool'] == selected_pool)]

if selected_pool != 'All':
    df_filteredschedule = df_filteredschedule[(df_filteredschedule['Pool'] == selected_pool)]

if selected_location != 'All':
    df_filteredschedule = df_filteredschedule[(df_filteredschedule['Location'] == selected_location)]

if played_val:
    df_filteredschedule = df_filteredschedule[df_schedule['T1G1'] == 0]

if game_scores:
    columns_to_show = ['Pool','Location','Court','Time','Team1','T1G1','T1G2','T1G3','Team2','T2G1','T2G2','T2G3']
else:
    columns_to_show = ['Pool','Location','Court','Time','Team1','Team2']

st.dataframe(df_filteredschedule,
             column_order=columns_to_show,
             column_config={
                            "Pool": st.column_config.TextColumn(
                                                                "P",
                                                                help="Pool",
                                                                width=None,
                                                                ),
                            "Location": st.column_config.TextColumn(
                                                                "L",
                                                                help="Location",
                                                                width=None
                                                                ),
                            "Court": st.column_config.TextColumn(
                                                                "C",
                                                                help="Court Number",
                                                                width=None
                                                                ),                                                             
                            },
                #width=800,
                hide_index=True
            )

import streamlit as st
import pandas as pd

st.set_page_config(
   page_title="Standings",
   page_icon='948',
   layout="wide",
   #initial_sidebar_state="expanded",
)

st.header("CURRENT STANDINGS")

df_schedule = pd.read_csv('static/schedule.csv')

wins = {}
losses = {}
l_teams = []

l_teams1 = df_schedule['Team1'].unique().tolist()
l_teams2 = df_schedule['Team2'].unique().tolist()
l_teams3 = l_teams1 + l_teams2

for t in l_teams3:
    if t not in l_teams:
        l_teams.append(t)

l_teams.sort()

# create keys with all team names

for team in l_teams:
    wins[team] = 0
    losses[team] = 0

st.write(wins)

# count them off

#for idx,row in df_full_schedule.iterrows():
#    winner = row['WinningTeam']
#    loser = row['LT']
#    wins[winner] +=1
#    losses[loser] +=1

# put them into a dataframe

st.dataframe(df_schedule,hide_index=True)

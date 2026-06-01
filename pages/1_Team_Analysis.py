import streamlit as st
import plotly.express as px
from utils.load_data import load_matches
from utils.helper import team_stats, team_wins, head_to_head


matches = load_matches()

st.title("🏏 Team Analysis")

teams = sorted(
    list(
        set(matches['team1']).union(
            set(matches['team2'])
        )
    )
)

selected_team = st.selectbox(
    "Select Team",
    teams
)

played, won, lost, win_percent = team_stats(
    matches,
    selected_team
)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Matches", played)
c2.metric("Wins", won)
c3.metric("Losses", lost)
c4.metric("Win %", win_percent)

st.markdown("---")

st.subheader("🏆 Team Wins Comparison")

wins_df = team_wins(matches)

fig = px.bar(
    wins_df,
    x="Team",
    y="Wins",
    title="IPL Team Wins (2008-2020)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
fig.update_layout(height=600)

st.markdown("---")

opponent_team = st.selectbox(
    "Select Opponent",
    [team for team in teams if team != selected_team]
)

st.markdown("---")

st.subheader("🤝 Head to Head Analysis")

matches_played, team1_wins, team2_wins = head_to_head(
    matches,
    selected_team,
    opponent_team
)

c1, c2, c3 = st.columns(3)

c1.metric(
    "Matches Played",
    matches_played
)

c2.metric(
    selected_team,
    team1_wins
)

c3.metric(
    opponent_team,
    team2_wins
)
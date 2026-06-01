import streamlit as st
import plotly.express as px

from utils.load_data import load_deliveries
from utils.helper import (
    bowler_stats,
    top_bowlers,
    top_economy_bowlers,
    top_dot_ball_bowlers,
    purple_cap
)

deliveries = load_deliveries()

st.title("🎯 Bowler Analysis")

bowlers = sorted(
    deliveries['bowler'].dropna().unique()
)

selected_bowler = st.selectbox(
    "Select Bowler",
    bowlers
)

wickets, balls, runs, economy = bowler_stats(
    deliveries,
    selected_bowler
)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Wickets", wickets)
c2.metric("Balls", balls)
c3.metric("Runs Conceded", runs)
c4.metric("Economy", economy)

st.markdown("---")

st.subheader("🎯 Top 10 Wicket Takers")

top_df = top_bowlers(deliveries)

fig = px.bar(
    top_df,
    x="Bowler",
    y="Wickets",
    title="Top 10 IPL Wicket Takers"
)

fig.update_layout(height=500)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

st.subheader("💰 Top Economy Bowlers")

eco_df = top_economy_bowlers(
    deliveries
)

fig2 = px.bar(
    eco_df,
    x="bowler",
    y="Economy"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.markdown("---")

st.subheader("🛑 Top Dot Ball Bowlers")

dot_df = top_dot_ball_bowlers(
    deliveries
)

fig3 = px.bar(
    dot_df,
    x="bowler",
    y="Dot Balls"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.markdown("---")

st.subheader("🧢 Purple Cap Leaderboard")

purple_df = purple_cap(
    deliveries
)

st.dataframe(
    purple_df,
    use_container_width=True
)
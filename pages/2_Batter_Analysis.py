import streamlit as st
import plotly.express as px

from utils.load_data import load_deliveries

from utils.helper import (
    batter_stats,
    top_batters,
    boundary_percentage,
    top_six_hitters,
    top_boundary_hitters,
    top_strike_rate_batters,
    orange_cap
)

deliveries = load_deliveries()

st.title("🏏 Batter Analysis")

batters = sorted(
    deliveries['batsman'].dropna().unique()
)

selected_batter = st.selectbox(
    "Select Batter",
    batters
)

runs, balls, fours, sixes, strike_rate = batter_stats(
    deliveries,
    selected_batter
)

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Runs", runs)
c2.metric("Balls", balls)
c3.metric("4s", fours)
c4.metric("6s", sixes)
c5.metric("Strike Rate", strike_rate)

st.markdown("---")

boundary_pct = boundary_percentage(
    deliveries,
    selected_batter
)

st.metric(
    "Boundary %",
    f"{boundary_pct}%"
)

st.markdown("---")

st.subheader("🏆 Top 10 IPL Run Scorers")

top_df = top_batters(deliveries)

fig = px.bar(
    top_df,
    x="Batter",
    y="Runs",
    title="Top 10 IPL Run Scorers"
)

fig.update_layout(height=500)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

st.subheader("🚀 Top 10 Six Hitters")

six_df = top_six_hitters(
    deliveries
)

fig2 = px.bar(
    six_df,
    x="batsman",
    y="Sixes",
    title="Top 10 IPL Six Hitters"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.markdown("---")

st.subheader("🔥 Top 10 Boundary Hitters")

boundary_df = top_boundary_hitters(
    deliveries
)

fig3 = px.bar(
    boundary_df,
    x="batsman",
    y="Boundaries",
    title="Top 10 IPL Boundary Hitters"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.markdown("---")

st.subheader("⚡ Top 10 Strike Rate Batters")

sr_df = top_strike_rate_batters(
    deliveries
)

fig4 = px.bar(
    sr_df,
    x="batsman",
    y="Strike Rate",
    title="Top 10 Strike Rate Batters (Min 500 Balls)"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.markdown("---")

st.subheader("🧢 Orange Cap Leaderboard")

orange_df = orange_cap(
    deliveries
)

st.dataframe(
    orange_df,
    use_container_width=True
)

if strike_rate >= 140:
    st.success("🚀 Aggressive Batter")

elif strike_rate >= 120:
    st.info("⚡ Balanced Batter")

else:
    st.warning("🛡️ Anchor Batter")
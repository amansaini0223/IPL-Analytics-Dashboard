import streamlit as st
import plotly.express as px

from utils.load_data import load_matches
from utils.helper import (
    venue_stats,
    venue_details,
    venue_match_type
)

matches = load_matches()

st.title("🏟️ Venue Analysis")

# ==========================
# Venue Selector
# ==========================

venues = sorted(
    matches['venue'].dropna().unique()
)

selected_venue = st.selectbox(
    "Select Venue",
    venues
)

total_matches, team, wins = venue_details(
    matches,
    selected_venue
)

# ==========================
# Metrics
# ==========================

st.markdown(f"""
### 🏆 Most Successful Team

# {team}
""")

c1, c2 = st.columns(2)

c1.metric(
    "Matches Played",
    total_matches
)

c2.metric(
    "Wins",
    wins
)

st.markdown("---")

# ==========================
# Top Venues Chart
# ==========================

st.subheader("🏟️ Top 10 IPL Venues")

venue_df = venue_stats(matches)

fig = px.bar(
    venue_df,
    x="Venue",
    y="Matches",
    title="Top 10 IPL Venues"
)

fig.update_layout(
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ==========================
# Venue Data Table
# ==========================

st.subheader("📋 Venue Statistics")

st.dataframe(
    venue_df,
    use_container_width=True
)
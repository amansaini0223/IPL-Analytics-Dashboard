import streamlit as st
from utils.load_data import load_matches, load_deliveries

st.set_page_config(
    page_title="IPL Analytics Dashboard",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

matches = load_matches()
deliveries = load_deliveries()

# ======================
# Title Section
# ======================

st.title("🏏 IPL Analytics Dashboard")

st.markdown("""
### IPL Data Analysis (2008–2020)

Explore team performance, batting records, bowling statistics,
venue insights and IPL records using interactive visualizations.
""")

st.markdown("---")

# ======================
# KPI Cards
# ======================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Matches",
        matches.shape[0]
    )

with col2:
    st.metric(
        "Teams",
        len(set(matches['team1']).union(set(matches['team2'])))
    )

with col3:
    st.metric(
        "Runs",
        f"{int(deliveries['total_runs'].sum()):,}"
    )

with col4:
    st.metric(
        "Wickets",
        f"{int(deliveries['is_wicket'].sum()):,}"
    )

st.markdown("---")

# ======================
# Dashboard Overview
# ======================

st.subheader("📌 Dashboard Overview")

st.info("""
This dashboard provides complete IPL analytics from 2008–2020.

✅ Team Analysis

✅ Batter Analysis

✅ Bowler Analysis

✅ Venue Analysis

✅ IPL Records
""")

st.markdown("---")

# ======================
# Dataset Information
# ======================

st.subheader("📁 Dataset Information")

c1, c2 = st.columns(2)

with c1:
    st.success(
        f"Matches Dataset : {matches.shape[0]} Matches"
    )

with c2:
    st.success(
        f"Ball-by-Ball Dataset : {deliveries.shape[0]:,} Deliveries"
    )

st.markdown("---")

# ======================
# Navigation Guide
# ======================

st.subheader("🧭 Navigation Guide")

st.markdown("""
Use the sidebar to explore:

- 🏏 Team Analysis
- 🏏 Batter Analysis
- 🎯 Bowler Analysis
- 🏟️ Venue Analysis
- 🏆 IPL Records
""")
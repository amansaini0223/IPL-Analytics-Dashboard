import streamlit as st

from utils.load_data import load_deliveries
from utils.helper import (
    most_runs,
    most_wickets,
    most_sixes,
    most_fours
)

deliveries = load_deliveries()

st.title("🏆 IPL Records")

c1, c2 = st.columns(2)
c3, c4 = st.columns(2)

runs = most_runs(deliveries)
wickets = most_wickets(deliveries)
sixes = most_sixes(deliveries)
fours = most_fours(deliveries)

c1.markdown("## 🏏 Highest Runs")
c1.markdown(f"# {runs.iloc[0]}")
c1.markdown(f"### 👤 {runs.index[0]}")

c2.markdown("## 🎯 Highest Wickets")
c2.markdown(f"# {wickets.iloc[0]}")
c2.markdown(f"### 👤 {wickets.index[0]}")

c3.markdown("## 6️⃣ Highest Sixes")
c3.markdown(f"# {sixes.iloc[0]}")
c3.markdown(f"### 👤 {sixes.index[0]}")

c4.markdown("## 4️⃣ Highest Fours")
c4.markdown(f"# {fours.iloc[0]}")
c4.markdown(f"### 👤 {fours.index[0]}")
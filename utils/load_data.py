import pandas as pd
import streamlit as st

@st.cache_data
def load_matches():

    matches = pd.read_csv("data/IPL Matches 2008-2020.csv")

    matches.replace({
        'Delhi Daredevils': 'Delhi Capitals',
        'Kings XI Punjab': 'Punjab Kings',
        'Rising Pune Supergiant': 'Rising Pune Supergiants'
    }, inplace=True)

    return matches


@st.cache_data
def load_deliveries():

    deliveries = pd.read_csv("data/IPL Ball-by-Ball 2008-2020.csv")

    deliveries.replace({
        'Delhi Daredevils': 'Delhi Capitals',
        'Kings XI Punjab': 'Punjab Kings',
        'Rising Pune Supergiant': 'Rising Pune Supergiants'
    }, inplace=True)

    return deliveries
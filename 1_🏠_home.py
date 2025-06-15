from datetime import datetime
import streamlit as st
import webbrowser
import pandas as pd

st.set_page_config(
    page_title="FIFA23 Official Dataset",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

if 'data' not in st.session_state:
    df_data = pd.read_csv('data/CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data'] = df_data

url_projeto = "https://github.com/thiagobrs/asimov-projects/tree/main/trilha1/curso10-fifa"
st.markdown("# FIFA23 OFFICIAL DATASET! ⚽")
st.sidebar.markdown(f"Developed by [Thiago Batista]({url_projeto})")

btn = st.button("Access the data on Kaggle")
if btn:
    url_kaggle = "https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data"
    webbrowser.open_new_tab(url_kaggle)

st.markdown(
    """
    ## About the Dataset
    The dataset contains official data from **FIFA 23**, including information about players, clubs, leagues, and performance
    statistics.

    ### Main Columns:
    - `player_name`: Player's name
    - `club`: Player's club
    - `league`: League in which the club competes
    - `overall_rating`: Player's overall rating
    - `potential`: Player's maximum potential
    - `age`: Player's age
    - `nationality`: Player's nationality

    ### Objectives:
    - Player performance analysis
    - Comparison between clubs and leagues
    - Identification of emerging talents
    """
)

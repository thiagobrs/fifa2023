import streamlit as st

st.set_page_config(
    page_title="FIFA23 Official Dataset",
    page_icon="⚽",
    layout="wide"
)

df_data = st.session_state.get('data', None)

clubs = sorted(df_data['Club'].unique())
club = st.sidebar.selectbox('Select a Club', clubs)

df_players = df_data[df_data['Club'] == club].sort_values(by='Name', ascending=False)
players = sorted(df_players['Name'].unique())
player = st.sidebar.selectbox('Select a Player', players)

player_data = df_players[df_players['Name'] == player].iloc[0]
st.image(player_data['Photo'])
st.markdown(f"# {player_data['Name']} <img src='{player_data['Flag']}'>", unsafe_allow_html=True)

st.markdown(f"**Club:** {player_data['Club']}")
st.markdown(f"**Position:** {player_data['Position']}")

col1, col2, col3 = st.columns(3)
col1.markdown(f"**Age:** {player_data['Age']}")
col2.markdown(f"**Height:** {player_data['Height(cm.)'] / 100} m")
col3.markdown(f"**Weight:** {player_data['Weight(lbs.)'] * 0.453:.2f} kg")
st.divider()

st.subheader(f"Overall Rating {player_data['Overall']}")
st.progress(int(player_data['Overall']))

col1, col2, col3 = st.columns(3)
col1.metric(label="Market Value", value=f"£{player_data['Value(£)']:,}")
col2.metric(label="Wage", value=f"£{player_data['Wage(£)']:,}")
col3.metric(label="Release Clause", value=f"£{player_data['Release Clause(£)']:,}")

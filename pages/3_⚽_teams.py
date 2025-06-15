import streamlit as st

st.set_page_config(
    page_title="FIFA23 Official Dataset",
    page_icon="⚽",
    layout="wide"
)

df_data = st.session_state.get('data', None)

clubs = sorted(df_data['Club'].unique())
club = st.sidebar.selectbox('Select a Club', clubs)
df_filtered = df_data[df_data['Club'] == club].set_index('Name').sort_index()
st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

columns = ["Photo", "Flag", "Overall", "Position", "Age", "Preferred Foot", "Height(cm.)", "Weight(lbs.)", "Value(£)", "Wage(£)",
           "Joined", "Contract Valid Until", "Release Clause(£)"]

st.dataframe(df_filtered[columns],
             column_config={
                 "Photo": st.column_config.ImageColumn("Photo", width="small"),
                 "Country": st.column_config.ImageColumn("Flag", width="small"),
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", min_value=0, max_value=100, format="%d"),
                 "Wage(£)": st.column_config.ProgressColumn(
                     "Weekly Wage", format="£%f", min_value=0, max_value=df_filtered["Wage(£)"].max()),
             })

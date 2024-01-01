import streamlit as st
import pandas as pd

# test_df = pd.DataFrame([40, 33, 25], ['gold', 'silver', 'bronze'])

athletes = pd.read_csv('backend/data/athletes.csv')
events = pd.read_csv('backend/data/events.csv')
st.title("**Olympics Data**")
col1, col2 = st.columns(2)
athletes_df = st.dataframe(athletes, height=500, width=1000)
events_df = st.dataframe(events, height=500, width=1000)
col1.write(athletes_df)
col2.write(events_df)


# conn = st.connection('olympics', type='psql')
# china_athletes = conn.query('select * from athletes where team = China;')
# st.dataframe(china_athletes)


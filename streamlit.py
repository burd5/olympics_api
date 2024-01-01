import streamlit as st
import pandas as pd
import altair as alt

conn = st.connection("postgresql", type="sql")

df = conn.query("""select team, 
                      SUM(CASE WHEN medal = 'Gold' THEN 1 else 0 end) as gold_medals,
                      SUM(CASE WHEN medal = 'Silver' THEN 1 else 0 end) as silver_medals,
                      SUM(CASE WHEN medal = 'Bronze' THEN 1 else 0 end) as bronze_medals,
                      SUM(CASE WHEN medal is not null then 1 else 0 end) as all_medals
                      from results 
                      group by 1
                      order by all_medals DESC
                      limit 20;""")

st.write(df)
scale = alt.Scale(domain=['gold_medals', 'silver_medals', 'bronze_medals'], range=['#FFD700', '#C0C0C0', '#CD7F32'])
chart = alt.Chart(df).transform_fold(
  fold=['gold_medals', 'silver_medals', 'bronze_medals'],
  as_=['column', 'value']
).mark_bar().encode(
  x='team:N',
  y='value:Q',
  color=alt.Color('column:N', scale=scale),
  order=alt.Order(
    'value:Q',
    sort='descending'
    )
).properties(
    width = 1400,
    height = 1000
)
st.write(chart)

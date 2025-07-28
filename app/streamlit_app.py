import streamlit as st
from sqlalchemy import text
from sqlalchemy.engine import create_engine
import pandas as pd

st.set_page_config(page_title="Plant-Virus-Atlas", layout="wide")

@st.cache_resource
def get_engine():
    conn = st.connection("postgres")
    return conn.session
engine = get_engine()

# ----- Sidebar filters -----
st.sidebar.header("Filters")
host_choice = st.sidebar.multiselect(
    "Host plant species",
    options=[row[0] for row in engine.execute(text("SELECT DISTINCT species_name FROM hosts ORDER BY species_name"))],
)
year = st.sidebar.slider("Isolation year", 1900, 2025, (2000, 2025))

# ----- Query -----
query = text("""
SELECT p.name AS pathogen,
       h.species_name AS host,
       p.sequence_type,
       p.isolation_year,
       g.country
FROM pathogens p
JOIN host_pathogen_interactions i ON i.pathogen_id = p.id
JOIN hosts h  ON i.host_id = h.id
JOIN geographical_data g ON g.pathogen_id = p.id
WHERE (:host_list IS NULL OR h.species_name = ANY(:host_list))
  AND p.isolation_year BETWEEN :y1 AND :y2
LIMIT 1000;
""")

df = pd.read_sql_query(
    query,
    engine,
    params=dict(
        host_list=host_choice if host_choice else None,
        y1=year[0],
        y2=year[1],
    ),
)

st.title("Plant-Virus-Atlas: Interactive Explorer")
st.write(f"**{len(df):,} records** match your filter.")

st.dataframe(df)

# Quick bar chart
st.bar_chart(df.groupby("isolation_year").size())

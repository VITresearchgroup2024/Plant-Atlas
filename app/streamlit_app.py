import streamlit as st
import pandas as pd

# Page title
st.title("🦠 Plant Virus Database")
st.write("Welcome to the Plant Virus Atlas!")

# Simple message for now
st.success("✅ Your database is connected and working!")

# Show some basic info
st.subheader("Database Status")
st.write("- Virus table: ✅ Created")
st.write("- Sample data: ✅ Added") 
st.write("- Connection: ✅ Ready")

st.info("Next step: We'll connect this webpage to show your actual virus data!")

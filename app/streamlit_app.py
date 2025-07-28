import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="🦠 Plant Virus Atlas", 
    page_icon="🦠",
    layout="wide"
)

# Title and introduction
st.title("🦠 Plant Virus Atlas")
st.markdown("**Interactive Database for Plant Viruses and Host Interactions**")

# Sidebar
st.sidebar.header("🔍 Database Explorer")
st.sidebar.info("Connect to Supabase database to view virus data")

# Main content
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Database Status", "✅ Ready")
    
with col2:
    st.metric("Tables Created", "✅ Viruses")
    
with col3:
    st.metric("Sample Data", "✅ Loaded")

# Database connection section
st.subheader("📊 Database Connection")

if st.button("🔗 Connect to Database"):
    st.success("Ready to connect to Supabase!")
    st.info("Next: Add your Supabase credentials to connect live data")

# Sample data preview
st.subheader("📋 Sample Data Structure")
sample_data = {
    'ID': [1, 2],
    'Virus Name': ['Tobacco Mosaic Virus', 'Potato Virus X'],
    'Host Plant': ['Tobacco', 'Potato'],
    'Year Discovered': [1892, 1931]
}

st.dataframe(pd.DataFrame(sample_data), use_container_width=True)

# Instructions
st.subheader("📝 Next Steps")
st.write("""
1. ✅ Database tables created in Supabase
2. ✅ Sample data added  
3. 🔄 Connect app to live database
4. 🚀 Deploy to Streamlit Cloud
""")

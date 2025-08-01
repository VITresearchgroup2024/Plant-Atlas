import streamlit as st
import pandas as pd
import plotly.express as px
import time

# 1. Page config (must be first Streamlit command)
st.set_page_config(
    page_title="🦠 Plant Virus Atlas",
    page_icon="🦠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS styling
def apply_custom_css():
    st.markdown("""
    <style>
    /* Background gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: #333;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Sidebar background */
    .css-1d391kg {
        background: linear-gradient(180deg, #2e7bcf 0%, #1e5799 100%);
        color: white;
    }

    /* Sidebar header */
    .css-1d391kg h2,
    .css-1d391kg label,
    .css-1d391kg .stMarkdown p {
        color: white;
    }

    /* Metrics container style */
    div[data-testid="metric-container"] {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        padding: 15px;
        margin: 5px 0;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }

    /* Buttons styling */
    .stButton > button {
        background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 25px;
        padding: 10px 25px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background: linear-gradient(45deg, #764ba2 0%, #667eea 100%);
        box-shadow: 0 6px 12px rgba(102, 126, 234, 0.5);
        transform: translateY(-2px);
    }

    /* Styled table */
    div.stDataFrame > div > div > table {
        border-collapse: separate !important;
        border-spacing: 0 15px !important;
        border-radius: 10px !important;
        overflow: hidden !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        background-color: white;
    }
    
    thead tr th {
        background-color: #667eea !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        padding: 12px !important;
    }

    tbody tr:hover {
        background-color: #f0f2f6 !important;
    }

    tbody tr td {
        padding: 12px !important;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

apply_custom_css()


# 3. Hero Section
st.markdown("""
<div style="text-align: center; padding: 20px 0;">
    <h1 style="color: #2e7bcf; font-size: 3rem; margin-bottom: 10px;">🦠 Plant Virus Atlas</h1>
    <p style="font-size: 1.3rem; color: #444; margin-top: 0;">
        🌱 Interactive Database for Plant Viruses and Host Interactions 🔬
    </p>
</div>
""", unsafe_allow_html=True)


# 4. Sidebar with Search and Filters
with st.sidebar:
    st.markdown("## 🔍 Database Explorer")
    search_term = st.text_input("🔎 Search viruses...", placeholder="Enter virus name")
    
    st.markdown("### 📊 Filter by Category")
    virus_type = st.selectbox("Virus Type", ["All", "DNA Viruses", "RNA Viruses", "Retroviruses"])
    host_plant = st.selectbox("Host Plant", ["All", "Agricultural Crops", "Trees", "Ornamental Plants"])
    
    
# 5. Metrics Section
col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

with col1:
    st.markdown("### 🎯 Database Overview")

with col2:
    st.metric("Database Status", "✅ Connected", delta="Online")

with col3:
    st.metric("Total Records", "47,411", delta="Updated")

with col4:
    st.metric("Virus Types", "47", delta="Genotypes")


# 6. Clickable GitHub Links Section with Buttons and Cards
st.markdown("---")
st.markdown("## 🗂️ Browse Pathogen & Vector Data")

categories = [
    {"name": "Bacteria", "icon": "🦠", "color": "#e74c3c", "count": "1,247"},
    {"name": "Fungi", "icon": "🍄", "color": "#f39c12", "count": "2,156"},
    {"name": "Viruses", "icon": "🦠", "color": "#9b59b6", "count": "3,892"},
    {"name": "Nematodes", "icon": "🪱", "color": "#27ae60", "count": "567"},
    {"name": "Oomycetes", "icon": "🌿", "color": "#2980b9", "count": "312"},
    {"name": "Protozoa", "icon": "🦠", "color": "#16a085", "count": "198"},
    {"name": "Viroids", "icon": "🧬", "color": "#8e44ad", "count": "131"}
]

cols = st.columns(len(categories) if len(categories) <= 5 else 5)  # Layout for max 5 cols

for i, category in enumerate(categories):
    col = cols[i % len(cols)]
    with col:
        st.markdown(f"""
        <div style="
            background: linear-gradient(45deg, {category['color']}22, {category['color']}11);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            border: 2px solid {category['color']}33;
            margin-bottom: 15px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        ">
            <h2 style="margin: 0; font-size: 2.5rem; color: {category['color']};">{category['icon']}</h2>
            <h3 style="margin: 10px 0; color: #333;">{category['name']}</h3>
            <p style="margin: 0; color: #666; font-weight: bold;">{category['count']} records</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"Browse {category['name']}", key=f"browse_{category['name']}"):
            url = f"https://github.com/VITresearchgroup2024/Plant-Atlas/tree/main/data/pathogen/{category['name'].lower()}"
            st.experimental_set_query_params()
            st.markdown(f"Opening [{category['name']}]({url}) in a new tab...")
            js = f"window.open('{url}')"
            st.components.v1.html(f"<script>{js}</script>", height=0, width=0)


# 7. Sample Data Table (Styled)
st.markdown("---")
st.subheader("📋 Sample Data Structure")

sample_data = {
    'ID': [1, 2, 3],
    'Virus Name': [
        'Tobacco Mosaic Virus', 
        'Potato Virus X', 
        'Cucumber Mosaic Virus'
    ],
    'Host Plant': ['Tobacco', 'Potato', 'Cucumber'],
    'Year Discovered': [1892, 1931, 1916]
}

df = pd.DataFrame(sample_data)

def create_styled_table(df):
    styled = df.style.format({'Year Discovered': '{:.0f}'})\
        .set_table_styles([
            {'selector': 'thead th', 'props': [
                ('background-color', '#667eea'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center'),
                ('font-size', '1rem')
            ]},
            {'selector': 'tbody td', 'props': [
                ('text-align', 'center'),
                ('padding', '12px'),
                ('font-size', '0.95rem')
            ]},
            {'selector': 'tbody tr:hover', 'props': [
                ('background-color', '#f0f2f6')
            ]},
        ])
    return styled

st.dataframe(create_styled_table(df))


# 8. Sample Data Visualization Section
st.markdown("---")
st.markdown("## 📊 Virus Distribution Overview")

col1, col2 = st.columns(2)

with col1:
    virus_data = {'Virus Type': ['DNA', 'RNA', 'Retrovirus'], 
                  'Count': [45, 67, 23]}
    fig_pie = px.pie(pd.DataFrame(virus_data), values='Count', names='Virus Type',
                     color_discrete_sequence=['#667eea', '#764ba2', '#f093fb'],
                     title='Virus Types')
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    host_data = {'Host': ['Crops', 'Trees', 'Ornamental'], 
                 'Count': [89, 34, 12]}
    fig_bar = px.bar(pd.DataFrame(host_data), x='Host', y='Count',
                     color_discrete_sequence=['#667eea'],
                     title='Host Plant Distribution')
    st.plotly_chart(fig_bar, use_container_width=True)


# 9. Interactive Buttons and Loading Animation
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔗 Connect to Database"):
        st.success("Connected to Supabase!")
        
with col2:
    if st.button("📊 View Analytics"):
        st.info("Analytics dashboard coming soon!")
        
with col3:
    if st.button("📥 Download Data"):
        st.info("Download feature available!")

# Loading Simulation
st.markdown("---")
st.markdown("### Loading progress demo")
progress_bar = st.progress(0)
status_text = st.empty()
for percent_complete in range(101):
    progress_bar.progress(percent_complete)
    status_text.text(f'Database loading... {percent_complete}%')
    time.sleep(0.01)
status_text.text('✅ Database loaded successfully!')


# 10. Footer
st.markdown("---")
st.markdown("<p style='text-align:center; color:#666; font-size:0.9rem;'>Built with ❤️ using Streamlit | © 2024 VIT Research Group</p>", unsafe_allow_html=True)

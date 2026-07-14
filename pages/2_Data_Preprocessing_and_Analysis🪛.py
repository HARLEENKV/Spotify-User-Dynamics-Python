import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import io

st.set_page_config(page_title="Spotify User Dynamics Dashboard", page_icon="🎶", layout="wide")
st.sidebar.title("Sidebar📂")
with st.sidebar:
  st.title("Navigation")
  st.page_link("app.py", label= 'Dashboard', icon='👩🏻‍💻')
  st.page_link("pages/1_Getting_Started🌱.py", label= 'Getting Started', icon='🌱')
  st.page_link("pages/2_Data_Preprocessing_and_Analysis🪛.py", label= 'Data Preprocessing and Analysis', icon='🪛')
  st.page_link("pages/3_EDA_on_Demographics🌍.py", label= 'EDA on Demographics', icon='🌍')
  st.page_link("pages/4_Subscription_Analysis💳.py", label= 'Subscription Analysis', icon='💳')
  st.page_link("pages/5_Behavioral_Patterns🎧.py", label= 'Behavioral Patterns', icon='🎧')
  st.page_link("pages/6_Churn_Analysis📈.py", label= 'Churn Analysis', icon='📈')
  st.page_link("pages/7_Correlation_Matrix📊.py", label= 'Correlation Matrix', icon='📊')
  st.page_link("pages/8_Key_Takeaways📋.py", label= 'Key Takeaways', icon='📋')
  st.page_link("pages/9_Summary✨.py", label= 'Summary', icon='✨')
  
st.markdown(
  """
<style>
/* Container styling for the expander */
div[data-testid="stExpander"] {
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    transition: all 0.3s ease-in-out;
}

/* Highlight effect on hover */
div[data-testid="stExpander"]:hover {
    border-color: #1DB954; /* Spotify Green */
    box-shadow: 0 4px 12px rgba(29, 185, 84, 0.2);
    background-color: rgba(255, 255, 255, 0.02);
}

/* Optional: Subtle glow when the expander is actually open */
div[data-testid="stExpander"][aria-expanded="true"] {
    border-color: rgba(255, 255, 255, 0.3);
}
</style>
""",
unsafe_allow_html=True
)


if 'df' not in st.session_state:
    st.session_state['df'] = pd.read_csv("Spotify_user_dataset.csv")
df = st.session_state['df']


st.header("Step-4 DATA PREPROCESSING🧐")
st.markdown("Dataset Information & Structural Properties")

buffer = io.StringIO()
df.info(buf=buffer)
info_summary = buffer.getvalue()

with st.expander("View Data Schema & Types (df.info)"):
    st.text(info_summary)


st.markdown("**STATISTICAL ANALYSIS📈**")
tab_numeric, tab_categorical = st.tabs(["🔢 Numerical Features", "🔤 Categorical Features"])
with tab_numeric:
    st.write("Summary statistics for numerical features:")
    st.dataframe(df.describe(), use_container_width=True)
with tab_categorical:
    st.write("Summary statistics for text/categorical features:")
    cat_features = df.describe(include=['object', 'category', 'O'])
    st.dataframe(cat_features, use_container_width=True)


st.header("STEP-5 DATA CLEANING🧹")

st.markdown("Checking for any missing values in the dataset using [df.isnull().sum()].")
missing_values = df.isnull().sum()
missing_df = pd.DataFrame({"Missing Values": missing_values})

if missing_values.sum() == 0:
    st.success("✅ No missing values found in the dataset.")
else:
    st.warning("⚠️ Missing values detected in the dataset:")


st.markdown("Checking for any duplicate values in the dataset using [df.duplicated().sum()].")
duplicates = df.duplicated().sum()

if duplicates == 0:
    st.success("✅ No duplicate values found in the dataset.")
else:
    st.warning(f"⚠️ Duplicate values detected in the dataset: {duplicates}")


st.header("STEP-6 EXPLORATORY DATA ANALYSIS🔍")
st.markdown(
    """
- EDA stands for Exploratory Data Analysis.
- It’s the process of examining and summarizing a dataset to understand its structure, spot patterns, detect anomalies, and form hypotheses before applying advanced modeling.
- Now let's explore the data through various visualizations in the upcoming sections to uncover patterns and insights in Spotify User Dynamics.
- By analyzing features such as listening time, skip rate, ads exposure, offline listening, subscription type, and demographics, the study identifies key drivers of churn and retention.
- The findings highlight actionable strategies for improving user satisfaction and loyalty.
"""
)

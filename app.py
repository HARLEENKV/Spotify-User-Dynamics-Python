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


st.title("SPOTIFY USER DYNAMICS🎶")
st.subheader("- A DATA SCIENCE PROJECT BY HARLEEN.")
st.write("Navigate through the sidebar to explore different aspects of Spotify User Dynamics and Behavior.")
st.image("zzz.png")


if 'df' not in st.session_state:
    st.session_state['df'] = pd.read_csv("Spotify_user_dataset.csv")


st.subheader("PROJECT OVERVIEW📘") 


with st.expander("**OBJECTIVE🎯**", expanded = True):
 st.write("The goal of this project is to perform **Exploratory Data Analysis (EDA) on Spotify user behavior** to uncover insights about listening patterns, engagement, and churn. By analyzing features such as skip rate, listening time, ads listened, offline listening, subscription type, and age, the project aims to identify the factors that influence user satisfaction and retention.")


with st.expander("**SCOPE OF ANALYSIS📊**"):
 st.markdown(
    """
- **User Engagement :**   Explore how listening time, skip rate, and songs per day vary across different subscription types.  
- **Subscription Insights :**   Compare Free vs Premium users in terms of age, offline listening, and ad exposure.  
- **Churn Analysis :**   Identify churned users, study their behavior, and highlight key predictors of churn.  
- **Feature Comparisons :**   Visualize relationships between features (skip rate vs listening time, ads vs churn, age vs churn).  
- **Retention Drivers :**   Highlight features like offline listening and reduced ads that encourage longer engagement.  
"""
)

with st.expander("**TOOLS AND TECHNIQUES🛠️**"):
 st.markdown(
    """
- **Python libraries :**   Numpy, Pandas, Seaborn, Matplotlib, Plotly for interactive visualizations.  
- **EDA methods :**   Line charts, Barplots, Distribution plots, KDE plots, heatmaps, area graphs, violin plots, and churn comparison charts.  
- **Business framing :**   Translate technical findings into actionable insights for understanding user patterns and retention strategies.  
"""
)

with st.expander("**EXPECTED OUTCOMES💡**"):
 st.markdown(
    """
- **Clear visualization** of how ads, skip rate, and offline listening impact churn.  
- **Identification** of user segments most at risk of churn.  
- **Professional insights** that connect data patterns to business decisions.  
- A **structured analysis** that can be extended into predictive modeling for churn prevention.  
"""
)

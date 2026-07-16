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
 

st.header("STEP-8  SUMMARY AND RETENTION KEYS✨")
st.info("⭐ Premium & Student tiers drive engagement, but Premium churn is a revenue risk.")
st.info("⭐ Free tier users are stable but highly variable in behavior.")
st.info("⭐ Skip rate and ads exposure are the strongest churn predictors.")
st.info("⭐ Younger users need targeted retention strategies; older users are more loyal.")
st.info("⭐ Ads vs Offline listening has the strongest inverse relationship, Offline listening is a clear retention driver.")
st.info("⭐ Churn itself requires multi‑feature modeling rather than single predictors.")

st.divider()
st.header("STEP-9  LIMITATIONS AND FUTURE SCOPE📈")
col1, col2 = st.columns(2)

with col1:
 with st.expander("**⛔ Limitations**"):
  st.markdown(
        """
        - Churn variable shows very weak linear correlations, so no single feature strongly predicts churn.
        - Dataset scope is limited (missing playlist creations, genre preferences, favorite artists/songs, social sharing features, etc).
        - Churn simplified as binary, not accounting for subscription cycles or inactivity nuances.
        - Balanced demographics may not fully reflect Spotify’s global user base.
        """
    )

with col2:
 with st.expander("**🚀 Future Work**"):
  st.markdown(
        """
        - Use advanced machine learning to capture non‑linear churn predictors.
        - Add richer features (playlist habits, genre preferences, social sharing).
        - Perform time‑series analysis to study trends and seasonal patterns.
        - Segment users into clusters for targeted retention strategies.
        - Build interactive dashboards for real‑time churn monitoring.
"""
    )

st.divider()
st.header("STEP-10 CONCLUSION✅")
st.markdown(
    """
This journey into **Spotify User Dynamics** shows that every listener’s story is unique — some thrive on Premium freedom, others stick with the Free Plan despite the ads, and many find comfort in offline playlists.
**While churn is shaped by skips and ads, retention grows from genuine engagement and connection.**
In the end, it’s not just about numbers, but about understanding people’s listening habits and finding ways to keep the music playing happily in their lives.
"""
)
st.markdown("<p style = 'text-align: center; color: #1DB954; font-size: 1.2rem; font-weight: bold;'>" 
            "Keep the music alive🎧, keep the listeners close❤️"
            "</p>",
            unsafe_allow_html=True)

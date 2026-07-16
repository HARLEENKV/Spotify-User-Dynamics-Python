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

st.title("📊CORRELATION ANALYSIS")


if 'df' in locals() or 'df'in globals():
    numeric_df = df.select_dtypes(include = ["number"])
    corr = numeric_df.corr()
    corr

with st.expander("**View Definition**"):
 st.markdown(
    """
 - Correlation analysis is a statistical method used to measure the strength and direction of the relationship between two variables.
 - Positive correlation → both variables increase together (e.g., listening time ↑, retention ↑).
 - Negative correlation → one increases while the other decreases (e.g., ads ↑, retention ↓).
 - No correlation → variables don’t show a consistent relationship.
 - The most common measure is the Pearson correlation coefficient (r), which ranges from -1 to +1:
     - +1 → perfect positive relationship
     - -1 → perfect negative relationship
     -  0 → no relationship
"""
)

st.divider()
st.subheader("CORRELATION MATRIX - KEY VARIABLES")
fig_corr = px.imshow(corr, text_auto=True, aspect = "auto", labels = dict(color="Correlation"), title = "Correlation Matrix", color_continuous_scale='RdBu_r')
st.plotly_chart(fig_corr, use_container_width=True)
with st.expander("**👉🏻VISUAL INSIGHTS :**"):
 st.markdown(
    """
- A correlation matrix is a table showing correlation coefficients between multiple variables at once.
- Rows and columns represent variables.
- Each cell shows the correlation value between two variables.
- Diagonal values are always 1 (a variable perfectly correlates with itself).
"""
)
with st.expander("**📊KEY INSIGHTS :**"):
 st.markdown("- Strong Negative Correlation(-0.88) : There is a significant inverse relationship between offline_listening and ads_listened_per_week. This suggests that users who listen to more music offline encounter far fewer advertisements, likely indicating they are on a premium or paid tier.")
 st.markdown("- Negligible Correlation with Churn : The target variable, is_churned, shows very weak correlations with all other features (ranging from -0.016 to 0.016). This indicates that no single metric in this list is a 'strong linear predictor' of whether a user will stop using the service.")
 st.markdown("- Feature Independence : Most features (like age, listening_time, and skip_rate) show correlations near zero with one another. This suggests these variables provide unique, non-redundant information for any further data modeling.")

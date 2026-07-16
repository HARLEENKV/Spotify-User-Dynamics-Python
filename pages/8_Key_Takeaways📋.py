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


st.header("STEP-7 KEY TAKEAWAYS📋")
st.markdown("A consolidation of analytical findings and insights from the Spotify User Dynamics Study.")


with st.expander("🎯**1. Demographics**", expanded = True):
    st.markdown(
        """
        - Gender : Balanced distribution across all three categories, no dominant majority.
        - Age : Wide range (16–60), fairly uniform counts (700-950 per bracket). Peaks at late teens/early 20s, age 30, and ages 45 & 55.
        - Country : High uniformity (954–1034 users). Australia (1034) and US (1032) lead; India (1011) and Germany (1015) show stable adoption.
        """
    )

with st.expander("🎯**2. Subscription Insights**", expanded = True):
    st.markdown(
        """
        - Age Distribution : Uniform across Free, Family, Premium, and Student tiers.
        - Student Plan : Mirrors Premium/Family age ranges, suggesting overlap in plan selection.
        - Listening Time :
            - Premium → highest (~156 units).
            - Family → slightly lower (~151 units), possibly due to shared accounts.
            - Free → widest variability (some very low, some very high).
            - Student → strong engagement, similar to Premium.
        """
    )

with st.expander("🎯**3. Behavioral Patterns**"):
    st.markdown(
        """
        - Songs Played : Median ~50/day across all tiers; Student tier slightly higher upper quartile.
        - Skip Rate : Stable across tiers (~30%), suggesting skips depend on content, not subscription.
        - Ads Exposure : Strictly limited to Free tier; wide variance (5–50 ads/week).
        - Listening Time Distribution : Mostly 100–200 minutes/day, stable across users.
        - Skip Rate Variability : Fluctuates heavily (0.25–0.35 baseline), no clear trend with songs played.
        - Device Type : Desktop leads (34.7%), Web (32.8%), Mobile (32.5%).
        - Offline Listening : Dominant among Premium users; broad session lengths (40–60 and 160–180 minutes common). Online streaming less frequent.
        """
    )


with st.expander("🎯**4. Churn Analysis**"):
    st.markdown(
        """
        - Retention : Free users dominate retained group (no cost barrier).
        - Churn Risk : Premium and Family show higher churn proportions — critical for revenue.
        - Student Plan : Strong retention, discount appears effective.
        - Listening Time : Active users have higher median listening times; churned users show lower engagement.
        - Skip Rate :
            - Active users → lower skip rates (0.2–0.4).
            - Churned users → very high skip rates (0.8–1.0).
            - Distinct clusters → skip rate is a strong churn predictor.
        - Age vs Churn :
            - Younger users (18–35) churn more.
            - Older users (45+) show higher stability.
            - Cross‑over point around mid‑age where retention overtakes churn.
        - Ads vs Churn :
            - Churned users → concentrated at 40–50 ads/week.
            - Retained users → clustered at 0–10 ads/week.
            - Minimal overlap → ads exposure is a high‑value churn predictor.
"""
    )

with st.expander("🎯**5. Correlation Insights**"):
    st.markdown(
        """
        - Offline Listening vs Ads : Strong negative correlation (-0.88) — offline listeners encounter far fewer ads, reflecting Premium/paid tiers.
        - Churn Variable : Very weak correlations (≈ -0.016 to 0.016) with all features, meaning no single metric strongly predicts churn.
        - Feature Independence : Most variables (age, listening_time, skip_rate) are nearly uncorrelated, providing unique, non‑redundant information for modeling.
        """
    )

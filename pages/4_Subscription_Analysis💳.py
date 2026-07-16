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

st.header("💳SUBSCRIPTION INSIGHTS")

st.divider()
col1, col2 = st.columns(2)
with col1:
 st.subheader("SKIP RATE COMPARISON")
 fig_skip = px.bar(df, x = "subscription_type", y = "skip_rate", color_discrete_sequence = px.colors.sequential.Viridis, color = "subscription_type", title = 'Skip Rate by Subscription Type')
 fig_skip.update_layout(xaxis_title="Subscription Type", yaxis_title='Skip Rate')
 plt.tight_layout()
 st.plotly_chart(fig_skip, use_container_width=True)
 with st.expander("**📊KEY INSIGHTS :**"):
   st.markdown("- Uniformity Across Tiers : The skip rate remains remarkably stable, ranging between 550-600 regardless of the subscription plan, however Premium tier has a higher skip rate possibly due to no ad constraints.")
   st.markdown("- Behavioral Consistency : This suggests that user skipping behavior is driven more by content or situational factors (like discovery playlists) rather than the financial model or features of the specific subscription tier.")


with col2:
 st.subheader("ADS LISTENED PER WEEK")
 fig_ads = px.scatter(df, x = "subscription_type", y = "ads_listened_per_week", color = "subscription_type", title = 'Ads listened per week by Subscription type', labels ={'subscription_type':'Subscription Type', 'ads_listened_per_week': "Ads Listened per Week"})
 st.plotly_chart(fig_ads, use_container_width=True)
 with st.expander("**📊KEY INSIGHTS :**"):
  st.markdown("- Targeted Ad Delivery : The visualization confirms that ad exposure is strictly limited to Free tier users. All other subscription types (Family, Premium, and Student) show zero ads listened to, indicating the premium model successfully removes advertisements.")
  st.markdown("- Usage Variance : Within the Free tier, there is a significant spread in ad consumption, ranging from 5 to nearly 50 ads per week. This suggests a wide range of engagement levels among non-paying users.")


st.divider()
col1, col2 = st.columns(2)
with col1:
 st.subheader("LISTENING TIME BY SUBSCRIPTION")
 fig_line = px.line(df, x = "subscription_type", y = "listening_time", markers = True, template = 'plotly_dark', title="Listening Time by Subscription Type", labels={'subscription_type': 'Subscription Type', 'listening_time': "Listening Time"})
 fig_line.update_traces(line=dict(width=0.05))
 st.plotly_chart(fig_line, use_container_width=True)
 with st.expander("**📊KEY INSIGHTS :**"):
   st.markdown("- Dominant Subscription Type : The Student subscription plan consistently shows the highest listening time, reaching up to 300 units (in minutes) on the y-axis.") 
   st.markdown("- Tiered Engagement : There is a clear correlation between subscription level and time spent on the platform. The hierarchy of listening time from highest to lowest is: Student (Highest), Premium, Family, Free(Lowest).") 
   st.markdown("- Low Engagement for Free Users: Users on the Free plan have the least listening time, remaining mostly near the 0–50 range on the y-axis.") 
   st.markdown("- Data Density: The visualization uses a dense vertical-line style, indicating a large volume of data points across all categories, with the most concentrated activity occurring in the Student and Premium segments.")


with col2:
 st.subheader("SONGS PER DAY COMPARISON")
 fig = px.box(df, x = "subscription_type", y = "songs_played_per_day", color = "subscription_type", title = "Songs per Day Comparison", labels = {"subscription_type":"Subscription Type",  "songs_played_per_day":"Songs played per Day"})
 st.plotly_chart(fig, use_container_width=True)
 with st.expander("**📊KEY INSIGHTS :**"):
  st.markdown("- Consistent Engagement : The median number of songs played is remarkably similar across all categories (Free, Family, Premium, and Student), hovering around 50 songs per day. This suggests that subscription tier is not a primary driver of daily volume and that each segment includes both low-engagement users and high-intensity \"power users.\"")
  st.markdown("- The Student group appears to have a slightly higher upper quartile compared to the others, suggesting a marginally higher concentration of high-volume listeners in that segment.")


st.divider()
st.subheader("AGE VS SUBSCRIPTION TYPE")
fig_violin = px.violin(df, x = "subscription_type", y = "age", color = "subscription_type", box = True, title = 'Age Distribution by Subscription Type', labels = {'subscription_type': "Subscription Type", 'age':"Age"} )
st.plotly_chart(fig_violin, use_container_width=True)
with st.expander("**📊KEY INSIGHTS :**"):
  st.markdown("- Uniform Age Distribution : Across all four subscription tiers—Free, Family, Premium, and Student—the distribution of ages is remarkably similar. Each category shows a broad, fairly rectangular distribution ranging from approximately 18 to 65 years old.")
  st.markdown("- Target Demographics : The \"Student\" category surprisingly mirrors the age range of the \"Premium\" and \"Family\" plans. This suggests that either the \"Student\" criteria are broad, or there is significant overlap in how different age groups select their plans.")

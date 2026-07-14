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

st.header("📌3. BEHAVIORAL PATTERNS")
st.divider()

st.subheader("LISTENING TIME VS AGE")
fig_violin_age = px.violin(df, x = "age", y = "listening_time", box = True, color = "age", title = "Listening Time vs Age", labels = {"age":"Age", "listening_time":"Listening Time"})
st.plotly_chart(fig_violin_age, use_container_width=True)
with st.expander("**📊KEY INSIGHTS :**"):
 st.markdown("- Symmetrical Profiles : The symmetry of each plot indicates a normal distribution within each age bracket, with no significant skewness toward extremely high or low listening times in any specific group.")
 st.markdown("- Narrow Range : The listening times are mostly concentrated between 100 and 200 units (in minutes), with very few data points extending toward 0 or above 300, showing a stable habit across the entire population shown.")


st.divider()
st.subheader("SKIP RATE VS SONGS PER DAY")
fig_line = px.scatter(df, x = "songs_played_per_day", y = "skip_rate",color = 'offline_listening', width=800,height=600, title = "Skip Rate vs Songs per Day", labels = {"songs_played_per_day":"Songs played per Day", "skip_rate": "Skip Rate"} )
st.plotly_chart(fig_line, use_container_width=True)
with st.expander("**📊KEY INSIGHTS :**"):
 st.markdown("- High Volatility : The skip rate shows significant fluctuations, indicating that user skipping behavior is highly variable and sensitive to factors beyond just the volume of songs played.")
 st.markdown("- Lack of Clear Trend : Data points are consistently spread from a skip rate of 0.0 to 0.6.There is no visible \"clustering\" where one group skips significantly more than others. This implies that user frustration (indicated by high skip rates) or passive listening (low skip rates) occurs relatively equally across all user segments shown.")
 st.markdown("- Offline Listening Density : The color gradient represents offline_listening (from 0 to 1).The mix of dark and light blue dots across the entire grid indicates that offline listening habits do not strictly dictate how much a user listens or how often they skip. Both high and low offline listeners are represented throughout the activity spectrum.")


st.divider()
st.subheader("OFFLINE LISTENING COMPARISON")
fig_density = px.density_heatmap(df, x = "offline_listening", y = "listening_time", title = "Offline Listening", labels = {"offline_listening":"Offline Listening", "listening_time":"Listening Time"}, color_continuous_scale = "Viridis")
st.plotly_chart(fig_density, use_container_width=True)
with st.expander("**👉🏻VISUAL INSIGHTS :**"):
 st.markdown(
    """
    - X-axis : Offline Listening (Binary 0 for Online/Streamed, 1 for Offline/Downloaded). 
    - Y-axis : Listening Time (measured in minutes, ranging from 0 to 250+).
    - Count : Represents the number of Users in the particular Listening Time Range.
    - Color Scale of Count : Dark purple represents low density (fewer instances i.e close to 100-150), while bright yellow/orange represents high density (more frequent instances i.e close to 400-450).
    """
)
with st.expander("**📊KEY INSIGHTS :**"):
 st.markdown(
    """
- Offline Dominance (Category 1) : The "1" column (Offline Listening) shows significantly higher density (yellow/orange areas) compared to the "0" column. This suggests that the user spends a much larger portion of their time listening to downloaded content than streaming online. 
- Lower Engagement in Online Streaming : The "0" column remains mostly dark purple throughout the scale, indicating that online streaming sessions are infrequent across all durations for this specific dataset.
- Broad vs. Specific Sessions: 
 	• Offline : Listening time is distributed across the entire 0–250 range, showing versatility in how downloaded music is consumed (both short and long sessions). 
	• Online : There are almost no significant clusters, suggesting online listening is likely incidental rather than a primary mode of consumption.
 - Contextual Conclusion : This pattern is typical of users with Premium accounts who utilize the offline download feature to save data or listen in areas with poor connectivity. The high count in the 40-60 and 160-180 range could represent a standard playlist length or a daily commute duration where offline music is the primary source of entertainment.
"""
)
 
 st.divider()
st.subheader("DEVICE TYPE USAGE")
device_counts = df['device_type'].value_counts()
fig_pie = px.pie(device_counts, values = device_counts.values, names = device_counts.index, color_discrete_sequence = px.colors.qualitative.Vivid, title = 'Device Type Usage')
st.plotly_chart(fig_pie, use_container_width=True)
with st.expander("**📊KEY INSIGHTS :**"): 
 st.markdown("- Desktop is the Leading Platform : It accounts for the largest share of usage at 34.7%.")
 st.markdown("- Web and Mobile are Nearly Even : Web usage follows closely at 32.8%, while Mobile usage represents 32.5%.")
 
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import io
import plotly.figure_factory as ff


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


st.header("📌4. CHURN ANALYSIS")

churned_users = df[df["is_churned"] == 1]
with st.expander("View raw data of churned users"):
     st.write(df["is_churned"].value_counts())
st.markdown(
    """
- Churn means when a user stops using a service or cancels their subscription.In Spotify’s case, churned users are those who either Cancel their premium subscription, or Stop being active on the platform for a certain period. It’s basically the opposite of retention.
- Churn analysis is the process of studying why users leave and identifying patterns that predict churn. It helps companies reduce user loss and improve retention.
- User churn status (1 = Churned, 0 = Active)
"""
)

st.divider()
col1, col2 = st.columns(2)
with col1:
 st.subheader("SUBSCRIPTION TYPE VS CHURN")
 fig_churn = px.histogram(df, x = "is_churned", color = "subscription_type", barmode= 'group', color_discrete_sequence=px.colors.qualitative.Set1, title = 'Churn by subscription Status', labels = {'is_churned':"Churned(1) vs Active(0)", "subscription_type":"Subscription Type",'count':"User Count"})
 st.plotly_chart(fig_churn, use_container_width=True)
 with st.expander("**📊KEY INSIGHTS :**"):
  st.markdown("- Retention is Dominated by \"Free\" Users : The Free plan has the highest count among users who have not churned. This suggests a large base of non-paying users who are relatively stable, likely because there is no financial cost to maintaining the account.")
  st.markdown(" - High Churn Risk in \"Premium\" and \"Family\" : When looking at the churned group, the Premium and Family segments show significant representation. While the total volume of retained users is high, the proportion of paid subscribers leaving is a critical concern for revenue stability.")
  st.markdown("- \"Student\" Plan Stability : The Student tier appears consistently across both categories but shows a very high retention-to-churn ratio. This indicates that the student discount is likely an effective retention tool, keeping younger users in the ecosystem with fewer cancellations.")


with col2:
 st.subheader("LISTENING TIME VS CHURN")
 fig_box = px.box(df, x = "is_churned", y = "listening_time", color = "subscription_type", title = "Listening Time Distribution by Churn Status", labels = {"is_churned":"Churned vs Active","listening_time":"Listening Time (minutes/day)"})
 st.plotly_chart(fig_box, use_container_width=True)
 with st.expander("**📊KEY INSIGHTS :**"):
  st.markdown("- Active Users (0) : The median listening time for active users (indicated by the horizontal line within the boxes on the left) is generally higher across all subscription types compared to churned users. This suggests that sustained higher daily listening time is a strong indicator of user retention.")
  st.markdown("- Churned Users (1) : Churned users exhibit a lower median and a more compressed interquartile range (the box itself), which indicates lower overall engagement before they discontinued the service.")
  st.markdown("- Premium & Student Tiers : These groups typically show higher total listening minutes. However, research indicates that the Student segment can be particularly volatile; they may also have higher churn risks due to budget sensitivity or lifestyle changes.")
  st.markdown("- Free Tier : This segment often has the widest spread of listening times but is highly susceptible to churn if ad exposure becomes excessive, leading to lower engagement patterns.")



st.divider()
col1,col2 = st.columns(2)
with col1:
 st.subheader("AGE VS CHURN")
 fig_area = px.area(df, x = "is_churned", y = "age", color = "is_churned", title = "Age VS Churn Comparison", labels = {"is_churned":"Churned (1) vs Active (0)","age":"Age"}, color_discrete_map = {"0":"blue","1":"red"})
 st.plotly_chart(fig_area, use_container_width=True)
 with st.expander("**📊KEY INSIGHTS :**"):
  st.markdown("- Higher Churn Among Younger Users : The dark shade range (Churned) is significantly wider at lower age brackets (roughly ages 18–35). This suggests that younger users are much more likely to leave the service. ")
  st.markdown("- Older Users are More Stable : As age increases, the light shade range (Active) expands while the light shade range (Churned) narrows. Users above the age of 45–50 appear to have a much higher retention rate. ")
  st.markdown("- The \"Cross-Over\" Point : There is a noticeable shift around the middle-age mark where the proportion of active users begins to overtake churned users. ")
  st.markdown("- Targeted Retention Opportunity : The data indicates a need for engagement strategies specifically tailored to younger demographics to reduce the high churn rate seen in the early stages of the age axis.")


with col2:
 st.subheader("ADS LISTENED PER WEEK VS CHURN")
 fig_violin = px.violin(df, x = "is_churned", y = "ads_listened_per_week", box = True, color = "is_churned", title = "Ads listened per Week by Churn status", labels = {"is_churned":"Churned (1) vs Active (0)","ads_listened_per_week":"Ads Listened per Week"})
 st.plotly_chart(fig_violin, use_container_width=True)
 with st.expander("**📊KEY INSIGHTS :**"):
  st.markdown("- Distinct Behavior Profiles : There is a stark contrast between the two groups. Retained users (0) and churned users (1) exhibit almost opposite listening behaviors regarding advertisements.")
  st.markdown("- High Ad Volume Correlates with Churn : Churned users are heavily concentrated at the top of the scale. Their distribution \"bulbs\" near 40–50 ads per week, suggesting that a high ad load is a primary driver or a strong indicator of user dissatisfaction.")
  st.markdown("- Low Ad Volume Correlates with Retention : Retained users are densely clustered at the bottom, typically listening to 0–10 ads per week. This suggests that a lighter ad experience is associated with long-term engagement.")
  st.markdown("- Minimal Overlap : The \"bulbs\" (areas of highest density) for both groups do not overlap. This lack of intersection makes ads_listened_per_week a high-value predictive feature for any machine learning model intended to identify users at risk of leaving.")
  st.markdown("- Outlier Behavior : While most retained users see few ads, the thin \"neck\" of the red violin shows that a small subset of loyal users tolerates high ad volumes without churning.")


st.divider()
active_users = df[df['is_churned'] == 0]['skip_rate']
churned_users = df[df['is_churned'] == 1]['skip_rate']
hist_data = [active_users, churned_users]
group_labels = ['Active (0)', 'Churned (1)']
colors = ['#3399FF', '#FF3333'] 

st.subheader("CHURN STATUS BY SKIP RATE")
fig_kde = ff.create_distplot(hist_data, group_labels, show_hist=False, colors=colors)
fig_kde.update_layout( title="Churn Status by Skip Rate", xaxis_title="Churned (1) VS Active (0)", yaxis_title="Skip Rate",  legend_title_text="Status")
st.plotly_chart(fig_kde, use_container_width=True)
with st.expander("**📊KEY INSIGHTS :**"):
 st.markdown("- High Early Correlation : At very low skip rates (near 1.0 on the x-axis), both \"Churned\" and \"Active\" users show a significant peak. This suggests that a large concentration of the user base, regardless of their eventual churn status, initially has low skip rates.")
 st.markdown("- Divergence Points : As the skip rate increases (moving from 1.0 toward 1.5), the density for \"Active\" users remains slightly higher than \"Churned\" users in certain mid-ranges, indicating that active users may be more likely to maintain moderate engagement.")
 st.markdown("- End-of-Spectrum Behavior : Both groups show a sharp decline in density as skip rates approach 1.5, suggesting that very high skip rates are relatively rare in this specific dataset.")
 st.markdown("- Peak Density for Churn : The \"Churned\" group has its highest concentration at a skip rate near 1.1. This could be a \"critical zone\" where users showing this specific level of skipping behavior are at their highest risk of leaving.")
 st.markdown("- Identifying At-Risk Users : Tracking changes in these engagement patterns (skip rates) acts as an early warning sign.")
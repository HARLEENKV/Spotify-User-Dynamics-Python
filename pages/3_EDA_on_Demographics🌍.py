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


st.header("🌍DEMOGRAPHICS ANALYSIS")
st.divider()

col1, col2 = st.columns(2)

with col1:
 st.subheader("GENDER DISTRIBUTION")
 gender_col = 'gender' if 'gender' in df.columns else 'Gender'
 if gender_col in df.columns:
     gender_counts = df[gender_col].value_counts().reset_index()
 gender_counts.columns = [gender_col, 'count']      

 fig_gender = px.pie(gender_counts, values = 'count', names = gender_col, color_discrete_sequence = px.colors.qualitative.Pastel, title = 'Gender Distribution')
 st.plotly_chart(fig_gender)
 with st.expander("**📊KEY INSIGHTS :**"):
  st.markdown("- Near-equal representation/Balanced distribution across all three gender categories.")
  st.markdown("- There is no dominant majority in the dataset.")

with col2:
 st.subheader("AGE DISTRIBUTION")
 age_col = 'age' if 'age' in df.columns else 'Age'
    
 if age_col in df.columns:
        fig_age = px.histogram(df, x = age_col, nbins=20, title ='Age Distribution', color_discrete_sequence =['orchid'], marginal = "rug")
        fig_age.update_layout(xaxis_title="Age", yaxis_title="Count",bargap=0.1)
        st.plotly_chart(fig_age)
 else:
        st.error("Age column not found in dataset.")

 with st.expander("**📊KEY INSIGHTS :**"): 
  st.markdown("- The dataset covers a wide age range, approximately from 15 to 60 years old, indicating a diverse user base, most age brackets maintain a consistent count between 700 and 950 individuals.")
  st.markdown("- While fairly uniform, there are distinct peaks in frequency at specific life stages :")
  st.markdown("    • Late Teens/Early 20s : High initial engagement.")
  st.markdown("    • Age 30 : A notable spike in users.")
  st.markdown("    • Ages 45, 55 : Recurring peaks in older demographics. ")

st.divider()
st.subheader("COUNTRY DISTRIBUTION")
country_col = 'country' if 'country' in df.columns else 'Country'
    
if country_col in df.columns:
        country_counts = df[country_col].value_counts()
        df_plot = country_counts.reset_index()
        df_plot.columns = ['Country', 'Count']
        full_names = ['Australia','United States','Germany','India','Pakistan', 'France','United Kingdom', 'Canada']
        label_map = dict(zip(df_plot['Country'], full_names))
        fig = px.bar(df_plot, x= 'Country', y = 'Count', title = 'Users per Country', color = 'Count', color_continuous_scale = 'Viridis', labels ={'Country': 'Country Name', 'Count': 'Count'})
        fig.update_layout(xaxis = dict(tickmode='array',tickvals=df_plot['Country'], ticktext = full_names))
        st.plotly_chart(fig, use_container_width=True)
else:
        st.error("Country column not found in dataset.")
with st.expander("**📊KEY INSIGHTS :**"):
  st.markdown("- High Performance Uniformity : The user counts are tightly clustered, ranging from a low of 954 (Canada) to a high of 1034 (Australia).")
  st.markdown("- Top Market Leaders : Australia (1034) and United States (1032) lead the group with the highest engagement numbers.")
  st.markdown("- Emerging Market Stability : India (1011) and Germany (1015) show nearly identical user counts, indicating stable adoption in these large markets.")

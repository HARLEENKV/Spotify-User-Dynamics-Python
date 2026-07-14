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


st.header("STEP-1 IMPORTING LIBRARIES👩🏻‍💻")
with st.expander("Click to view the libraries used in this project"):
    st.code(
    """
    import streamlit as st
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly.express as px
    """, language = "python"
    )

st.header("STEP-2 LOADING THE DATASET🔃")
st.caption("**DATASET SOURCE -**(https://www.kaggle.com/datasets/shree0910/spotify-user-dataset/data)")


@st.cache_data
def load_data():
    df = st.session_state['df']
    return df

try:
    df = load_data()
    st.success("☑️Dataset loaded successfully into the application context!")
    st.markdown("With the dataset successfully loaded, we now have access to key user attributes such as subscription type, listening time, skip rate, ads exposure, offline listening, and churn status, etc.")


    st.header("STEP-3 READING THE DATASET👀")

    rows, cols = df.shape
    st.metric(label = "Number of rows", value = rows)
    st.metric(label = "Number of Columns", value = cols)

    with st.expander("👉🏻View Dataset Columns"):
       st.write(list(df.columns))

    st.subheader("Dataset Preview")
    preview_option = st.radio("Choose preview option:", ["First 20 rows (Head)", "Last 20 rows (Tail)"]) 
    if preview_option == "First 20 rows (Head)":
        st.dataframe(df.head(20), use_container_width=True)
    else:
        st.dataframe(df.tail(20), use_container_width=True)

except FileNotFoundError:
    st.error("❌Dataset file not found. Please ensure 'Spotify_user_dataset.csv' is in the correct directory.")


with st.expander("**👉🏻COLUMN DESCRIPTIONS**"):
 st.markdown(
    """
    "USER_ID": Unique identifier for each Spotify user.\n
    "GENDER": Gender of the user.\n
    "AGE": Age of the user.\n
    "COUNTRY": User’s geographical location.\n
    "SUBSCRIPTION_TYPE": Type of Spotify subscription (Free / Premium).\n
    "LISTENING_TIME": Average daily listening time (in minutes).\n
    "SONGS_PLAYED_PER_DAY": Number of tracks played per day by the user.\n
    "SKIP_RATE": The percentage of tracks a user skips rather than listening to them completely.\n
    "DEVICE_TYPE": Primary device used for listening (Mobile, Desktop, etc).\n
    "ADS_LISTENED_PER_WEEK": Number of ads a user hears in a typical week.\n
    "OFFLINE_LISTENING": Indicates whether the user listens offline (1 = Yes, 0 = No).\n
    "IS_CHURNED": User churn status (1 = Churned, 0 = Active).\n
  """
 )
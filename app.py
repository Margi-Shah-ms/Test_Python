import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Page Configuration
st.set_page_config(
    page_title="Fitness Tracker Dashboard",
    page_icon="🏋️‍♂️",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

FILE_PATH = "fitness_activities.csv"

# Function to load data safely
@st.cache_data
def load_data():
    if os.path.exists(FILE_PATH):
        df = pd.read_csv(FILE_PATH)
    else:
        # Initial dummy structure if file doesn't exist
        df = pd.DataFrame(columns=['Date', 'Activity Type', 'Duration (Minutes)', 'Calories Burned'])
        df.to_csv(FILE_PATH, index=False)
    return df

df = load_data()

# App Header
st.title("🏋️‍♂️ Personal Fitness Tracker & Analytics")
st.caption("Track your daily workout routines, calories burned, and analyze health metrics.")

# Sidebar - Logging New Activity
st.sidebar.header("➕ Log New Activity")
with st.sidebar.form("log_form", clear_on_submit=True):
    activity_type = st.text_input("Activity Type (e.g., Running, Cycling, Gym)")
    duration = st.number_input("Duration (Minutes)", min_value=1.0, step=1.0)
    calories = st.number_input("Calories Burned", min_value=1.0, step=1.0)
    date = st.date_input("Date")
    
    submit_button = st.form_submit_button("Add Activity")

if submit_button:
    if activity_type.strip() == "":
        st.sidebar.error("Please enter a valid activity type.")
    else:
        new_row = pd.DataFrame([{
            'Date': str(date),
            'Activity Type': activity_type.strip().capitalize(),
            'Duration (Minutes)': int(duration),
            'Calories Burned': int(calories)
        }])
        
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(FILE_PATH, index=False)
        st.cache_data.clear()
        st.sidebar.success(f"Successfully added '{activity_type}'!")
        st.rerun()

# Check if dataset is empty
if df.empty:
    st.info("No activity records found! Use the sidebar to log your first workout session.")
else:
    # Calculations
    df['Calories per Minute'] = df['Calories Burned'] / df['Duration (Minutes)']
    total_calories = int(df['Calories Burned'].sum())
    avg_duration = round(df['Duration (Minutes)'].mean(), 1)
    total_activities = len(df)
    
    # Top KPI Metrics Row
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Workouts", f"{total_activities}")
    m2.metric("Total Calories Burned", f"{total_calories} kcal")
    m3.metric("Avg Duration", f"{avg_duration} mins")
    m4.metric("Avg Burn Rate", f"{round(df['Calories per Minute'].mean(), 1)} kcal/min")
    
    st.markdown("---")

    # Main Tabs
    tab1, tab2, tab3 = st.tabs(["📊 Analytics & Visualizations", "🔍 Filter & Data Table", "📋 Summary Report"])

    with tab1:
        st.subheader("Visual Analytics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Time Spent per Activity Type**")
            fig1, ax1 = plt.subplots(figsize=(6, 4))
            sns.barplot(x='Activity Type', y='Duration (Minutes)', data=df, ax=ax1, palette='Blues_d')
            plt.xticks(rotation=45)
            st.pyplot(fig1)

            st.write("**Activity Distribution**")
            fig2, ax2 = plt.subplots(figsize=(6, 4))
            activity_counts = df['Activity Type'].value_counts()
            ax2.pie(activity_counts, labels=activity_counts.index, autopct='%1.1f%%', startangle=90)
            st.pyplot(fig2)

        with col2:
            st.write("**Calories Burned Over Time**")
            fig3, ax3 = plt.subplots(figsize=(6, 4))
            df_sorted = df.sort_values('Date')
            ax3.plot(df_sorted['Date'], df_sorted['Calories Burned'], marker='o', color='orange', linewidth=2)
            plt.xticks(rotation=45)
            st.pyplot(fig3)

            st.write("**Correlation: Duration vs Calories**")
            fig4, ax4 = plt.subplots(figsize=(6, 4))
            sns.heatmap(df[['Duration (Minutes)', 'Calories Burned']].corr(), annot=True, cmap='coolwarm', ax=ax4)
            st.pyplot(fig4)

    with tab2:
        st.subheader("Interactive Activity Filter")
        
        activities = ["All"] + list(df['Activity Type'].unique())
        selected_activity = st.selectbox("Filter by Activity Type:", activities)
        
        if selected_activity != "All":
            filtered_df = df[df['Activity Type'].str.lower() == selected_activity.lower()]
        else:
            filtered_df = df
            
        st.write(f"Showing **{len(filtered_df)}** record(s)")
        st.dataframe(filtered_df, use_container_width=True)

    with tab3:
        st.subheader("Health & Fitness Summary Report")
        
        st.markdown(f"""
        - **Total Sessions Recorded:** `{total_activities}`
        - **Highest Calorie Workout:** `{df.loc[df['Calories Burned'].idxmax()]['Activity Type']}` ({df['Calories Burned'].max()} kcal)
        - **Longest Session:** `{df.loc[df['Duration (Minutes)'].idxmax()]['Activity Type']}` ({df['Duration (Minutes)'].max()} mins)
        - **Overall Calorie Output:** `{total_calories}` kcal
        """)
        
        st.write("**Full Dataset Breakdown:**")
        st.dataframe(df.describe().T, use_container_width=True)
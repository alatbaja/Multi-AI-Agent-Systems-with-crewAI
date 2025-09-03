import streamlit as st, pandas as pd, json, os

st.title("📊 CrewAI eCommerce Dashboard")
log_file = "logs/crew_run.json"
if os.path.exists(log_file):
    df = pd.read_json(log_file, lines=True)
    st.dataframe(df)
else:
    st.info("No logs yet. Run the crew to see data.")

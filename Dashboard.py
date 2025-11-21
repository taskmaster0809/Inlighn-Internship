import streamlit as st

def dashboard_page():
    st.title("E-Commerce Dashboard")

    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiNWJlZmE2ZjYtYTQwYi00ZDcxLTkzOGMtYTIwNTFmNWY0MWNlIiwidCI6IjMxY2MwODdiLWJhNDQtNGMyOS1hNmRkLWZkZjYwMDk0ZjNiZiJ9"

    st.markdown(
        f"""
        <iframe 
            src="{power_bi_url}" 
            width="100%" 
            height="600" 
            frameborder="0" 
            allowfullscreen="true">
        </iframe>
        """,
        unsafe_allow_html=True
    )

dashboard_page()

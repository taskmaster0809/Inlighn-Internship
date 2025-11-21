import streamlit as st

power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiNWJlZmE2ZjYtYTQwYi00ZDcxLTkzOGMtYTIwNTFmNWY0MWNlIiwidCI6IjMxY2MwODdiLWJhNDQtNGMyOS1hNmRkLWZkZjYwMDk0ZjNiZiJ9"

st.markdown(
    f"""
    <iframe 
        src="{power_bi_url}" 
        width="100%" 
        height="500" 
        frameborder="0" 
        allowfullscreen="true">
    </iframe>
    """,
    unsafe_allow_html=True
)


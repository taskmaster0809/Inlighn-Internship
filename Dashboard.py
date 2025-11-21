import streamlit.components.v1 as components

def dashboard_page():
    st.title("E-Commerce Dashboard")

    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiNWJlZmE2ZjYtYTQwYi00ZDcxLTkzOGMtYTIwNTFmNWY0MWNlIiwidCI6IjMxY2MwODdiLWJhNDQtNGMyOS1hNmRkLWZkZjYwMDk0ZjNiZiJ9"

    components.html(
        f"""
        <iframe 
            src="{power_bi_url}" 
            width="100%" 
            height="600" 
            style="border:none;">
        </iframe>
        """,
        height=650,
    )

dashboard_page()

def dashboard_page():
    st.title("E-Commerce Dashboard")
    # st.write(f"Welcome **{st.session_state['current_user']}**! Air Quality Index Dashboard!")

    # Power BI Embed URL
    power_bi_url = "https://app.powerbi.com/groups/me/reports/6e8ae584-e2a0-4594-8f93-2c8f72faede9?experience=power-bi"

    # Embed Power BI Dashboard using iframe
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

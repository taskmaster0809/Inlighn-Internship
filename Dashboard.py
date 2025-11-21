def dashboard_page():
    st.title("📊 AQI Dasboard (2018 - 22)")
    st.write(f"Welcome **{st.session_state['current_user']}**! Air Quality Index Dashboard!")

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

    # Sign-out button
    if st.button("Sign Out"):
        st.session_state["authenticated"] = False
        st.session_state["current_user"] = None
        st.experimental_rerun()

# Main App Logic
def main():
    # Initialize session state for authentication and user management
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if "current_user" not in st.session_state:
        st.session_state["current_user"] = None
    if "users" not in st.session_state:
        st.session_state["users"] = {}  # Store users as username: password

    # Navigation between Sign In and Sign Up
    menu = ["Sign In", "Sign Up"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if st.session_state["authenticated"]:
        dashboard_page()
    elif choice == "Sign In":
        login_page()
    elif choice == "Sign Up":
        signup_page()

# Run the Streamlit App
if __name__ == "__main__":
    main()

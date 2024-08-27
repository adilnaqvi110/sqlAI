import streamlit as st

st.set_page_config(
    page_title="SQL AI Query Generator",
    page_icon=":material/home:",
    layout="wide",
    initial_sidebar_state="auto"
)

if "api_key_value" not in st.session_state:
    st.session_state["api_key_value"]=""

# Custom CSS for the announcement bar
st.markdown(
    """
    <style>
    .announcement-bar {
        background-color: #f39c12;  /* Background color for the announcement bar */
        color: white;  /* Text color */
        padding: 10px;  /* Padding inside the bar */
        text-align: center;  /* Center the text */
        font-weight: bold;  /* Make the text bold */
        font-size: 18px;  /* Increase the font size */
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000;  /* Ensure it stays on top of other elements */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add the announcement text
st.markdown('<div class="announcement-bar">📢 Important Announcement: The system will be down for maintenance from 2 AM to 4 AM.</div>', unsafe_allow_html=True)

homePage = st.Page("src/Home.py",title="Home",default=True,icon=":material/home:")
scndPage = st.Page("src/Generate_SQL_Query.py",title="SQL AI",url_path="sql-ai",icon=":material/build:")
database = st.Page("src/db.py",title="Connect Database",url_path="connect-db",icon=":material/database:")

pages = [homePage,scndPage,database]
curPage = st.navigation(pages=pages,position="sidebar")

curPage.run()
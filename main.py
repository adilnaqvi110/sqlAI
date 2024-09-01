import streamlit as st

st.set_page_config(
    page_title="SQL AI Query Generator",
    page_icon=":material/home:",
    layout="wide",
    initial_sidebar_state="auto"
)

if "api_key_value" not in st.session_state:
    st.session_state["api_key_value"]=""

homePage = st.Page("src/Home.py",title="Home",default=True,icon=":material/home:")
scndPage = st.Page("src/Generate_SQL_Query.py",title="SQL AI",url_path="sql-ai",icon=":material/robot:")
database = st.Page("src/db.py",title="Connect Database",url_path="connect-db",icon=":material/database:")
executeSQL = st.Page("src/exec_sql.py",title="Execute SQL",url_path="execute",icon=":material/build:")

pages = [homePage,scndPage,database,executeSQL]
curPage = st.navigation(pages=pages,position="sidebar")

curPage.run()
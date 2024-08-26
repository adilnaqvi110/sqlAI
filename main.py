import streamlit as st

st.set_page_config(
    page_title="SQL AI Query Generator",
    page_icon=":material/home:",
    layout="wide",
    initial_sidebar_state="auto",
)

homePage = st.Page("src/Home.py",title="Home",default=True)
scndPage = st.Page("src/Generate_SQL_Query.py",title="SQL AI",url_path="sql-ai")

pages = [homePage,scndPage]

curPage = st.navigation(pages=pages,position="sidebar")
curPage.run()
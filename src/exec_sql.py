from views import execute_sql_query
import streamlit as st
import os

with st.sidebar:
    dbs = ["SQLite3","PostgreSQL","MySQL"]
    selectedDB = st.selectbox(label="Selected Database",options=dbs)
    MultiToggle = st.checkbox("Multi Query Execution")

st.title("SQLite Query Executor")

# Input text area to write SQL query
query = st.text_area("Enter your SQL query:", height=100)

pwd = os.getcwd()
db_fp = pwd + "data\db.sqlite3"

if st.button("Execute"):
    if query.strip():
        # Execute the query and get the result
        if selectedDB=="SQLite3":
            result_df = execute_sql_query(db_fp,query)
            st.write("Query Result:")
            st.dataframe(result_df)
            if result_df is None:
                st.success("Query Executed")
        else:
            st.write("Selected DB button works")
    else:
        st.error("Please enter a valid SQL query.")


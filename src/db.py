import streamlit as st
import sqlite3
import pandas as pd

# Main function to create the page
st.title("Connect to a Database 🗄️",anchor=False)
st.write("Select a database from the grid below and fill in the connection details.")

# Step 1: Display the database selection grid
databases = [
    {"name": "PostgreSQL", "type": "postgres"},
    {"name": "MySQL", "type": "mysql"},
    {"name": "SQLite3", "type": "sqlite"},
    {"name": "MongoDB", "type": "mongodb"},
    {"name": "Oracle", "type": "oracle"},
    {"name": "SQL Server", "type": "sqlserver"}
]

db_types = ["PostgreSQL","SQLite3","MySQL"]

left_col,right_col = st.columns([0.22,0.78])
with left_col:
    selected_db = st.selectbox(options=db_types,label="Select a Database:")

with right_col:
    if selected_db in ["PostgreSQL","MySQL"]:
        st.warning("In development..(Try SQLite3)")
        col1,col2 = st.columns([0.5,0.5])
        with col1:
            host = st.text_input("Host:")
            port = st.text_input("Port:")
        with col2:
            database = st.text_input("Database Name:")
            username = st.text_input("Username:")
        password = st.text_input("Password:", type="password")

    elif selected_db == "SQLite3":
        uploaded_file = st.file_uploader("Upload your SQLite database", type=["sqlite", "db","sqlite3"])
        if uploaded_file is not None:
            with open("data/temp_database.db", "wb") as f:
                f.write(uploaded_file.read())
            
            # Connect to the database
            conn = sqlite3.connect("temp_database.db")
            
            # Get the table names
            tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
            st.write("Tables in the database:", tables)
            
            # Close the connection
            conn.close()
    else:
        print("Selected database not available")
        
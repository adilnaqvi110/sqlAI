import streamlit as st

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

db = ["Postgres","SQLite3","MongoDB"]

left_col,right_col = st.columns([0.22,0.78])
with left_col:
    selected_db = st.selectbox(options=db,label="Select a Database:")

with right_col:
    if selected_db in ["Postgres", "SQLite3", "sqlserver"]:
        col1,col2 = st.columns([0.5,0.5])
        with col1:
            host = st.text_input("Host:")
            port = st.text_input("Port:")
        with col2:
            database = st.text_input("Database Name:")
            username = st.text_input("Username:")
        password = st.text_input("Password:", type="password")

    elif selected_db == "SQLite":
        filepath = st.text_input("Database File Path:")

    elif selected_db == "MongoDB":
        connection_uri = st.text_input("Connection URI:")
        
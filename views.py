import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import sqlite3
import pandas as pd

#Initialize model when LLM API key is provided
@st.cache_resource # avoids re-initializing the model everytime a page loads
def init_model(api_key):
    genai.configure(api_key=api_key)

    generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config
    )

    return model

# Extract the Latest SQL query from the model response
def extract_sql(response):
    data = response.text
    sqlStartIndex = data.find("```sql")
    sqlEndIndex = data.find("```",sqlStartIndex+6)

    if sqlStartIndex!=-1 and sqlEndIndex!=-1:
        sql_query = data[sqlStartIndex+6:sqlEndIndex]
    else:
        return 400
    
    return sql_query

def execute_sql_query(db_path: str, query: str):
    """
    Executes an SQL query on the specified SQLite database.

    Parameters:
    db_path (str): Path to the SQLite database file.
    query (str): The SQL query to execute.

    Returns:
    pd.DataFrame: DataFrame containing results if the query is a SELECT statement.
    str: Success or error message if the query is an action query (INSERT, UPDATE, DELETE, etc.).
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Determine the type of query (SELECT or action query)

        if "SELECT".lower() in query:
            # If the query is a SELECT statement, return the results as a DataFrame
            df = pd.read_sql(query, conn)
            print(df)
            return df
        else:
            # If the query is an action query, execute it
            cursor.execute(query)
            conn.commit()
            print("Query executed successfully!")
            return None
    except sqlite3.Error as e:
        # If there is an error, return the error message
        print(f"An error occurred: {e}")
    finally:
        # Close the database connection
        conn.close()
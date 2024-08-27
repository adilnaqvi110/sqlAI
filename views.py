import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

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

    sql_query = data[sqlStartIndex+6:sqlEndIndex]

    return sql_query

def execute_sql():
    pass

def connect_db(db_details):
    pass
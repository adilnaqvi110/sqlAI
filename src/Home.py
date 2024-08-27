import streamlit as st
import time

with st.sidebar:
    st.sidebar.title("SQL AI 🤖")
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("Welcome to the SQL AI Query Generator")
st.header("What is SQL AI Query Generator?")
st.write("""
The SQL AI Query Generator is an intelligent tool that helps you create SQL queries using natural language.
No need to worry about the complexities of SQL syntax. Just type your query in plain English,
and let the AI do the rest!
""")

st.header("To Get Started")
st.write("Make sure you already have an API key for your Google GEMINI model")

api_key_value = st.text_input(label="Enter your API key here:",type="password",placeholder="Press enter to register API key")

if st.button(label="Try it!"):
    st.session_state["api_key_value"]=api_key_value
    time.sleep(0.3)
    st.switch_page("src/Generate_SQL_Query.py")

if "api_key_value" in st.session_state and st.session_state["api_key_value"]!="":
    st.caption("API key Status: ✅")

st.header("How It Works")
st.write("""
1. **Input Your Query:** Simply type what you want to do with your data in natural language.
For example, "Show me all employees who were promoted last year."

2. **AI-Powered Query Generation:** The AI understands your request and converts it into an SQL query.

3. **Execute or Modify:** You can run the generated query directly or modify it to suit your needs.

4. **Get Results:** View the results directly in the interface, and gain insights from your data effortlessly.

Whether you're a beginner or an experienced SQL user, this tool saves time and makes data querying accessible to everyone.
""")

st.caption("Tip: You can start by typing a simple query like 'List all employees in the Sales department.' and see the AI in action!")
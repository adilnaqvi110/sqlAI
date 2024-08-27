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

def home():
    st.title("Welcome to the SQL AI Query Generator")
    st.header("What is SQL AI Query Generator?")
    st.write("""
    The SQL AI Query Generator is an intelligent tool that helps you create SQL queries using natural language.
    No need to worry about the complexities of SQL syntax. Just type your query in plain English,
    and let the AI do the rest!
    """)
    if st.button(label="Try it!"):
        st.switch_page("pages/Generate_SQL_Query.py")

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

def query_gen():
    with st.sidebar:
        api_key = st.text_input("GEMINI API Key", key="chatbot_api_key", type="password")
        
    if not api_key:
        st.title("Enter your API key to activate the Query Generator")

    model = init_model(api_key)

    if api_key:
        st.title("💬 Chatbot")
        st.caption("🚀 A SQL query generator powered by Gemini")
        if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

        if prompt := st.chat_input(placeholder="Ask your query here :)"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            response = model.generate_content(prompt)
            sql_query = extract_sql(response)
            print(sql_query)
            if sql_query==400:
                msg = "You have not entered any question regarding an SQL query, please ask me questions only regarding a query that you want to generate :)"
                st.session_state.messages.append({"role": "assistant", "content": msg})
                st.chat_message("assistant").write(msg)
            else:
                msg = response.text
                st.session_state.messages.append({"role": "assistant", "content": msg})
                st.chat_message("assistant").write("```sql"+sql_query+"```")

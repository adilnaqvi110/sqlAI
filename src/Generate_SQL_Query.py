import streamlit as st
from views import init_model,extract_sql
from dotenv import load_dotenv
import os
import streamlit_shadcn_ui as ui

load_dotenv()

with st.sidebar:
    # api_key = st.text_input(placeholder="Enter your API key here",label="", type="password")
    # st.caption("Note: Right now the chat window disappersif pagesare switched, reneter API key to get it back")
    reset_chat = st.button("Reset Chat",key="reset_chat_button")
    st.title("How to use SQL AI",anchor=False)
    st.write("""
1. **Generate SQL Query**: In the SQL Generator chatbox, type your required SQL query in natural language.
2. **Output SQL Query**: The AI model generates an SQL as per your input.
3. **View Results**: The results of your query will be displayed code box within chat.
4. **Check Syntax**: Check the syntax of the query to ensure your SQL query is correct before execution.
""")
    
if st.session_state["api_key_value"]=="":
    st.warning("API key not initialized")
    st.caption("Tip: Visit the Home page and enter the API key for your model")

# api_key = os.getenv("GEMINI_API_KEY")
if "api_key_value" in st.session_state and st.session_state["api_key_value"]!="":
    model = init_model(st.session_state["api_key_value"])
    st.title("💬 Chatbot",anchor=False)
    st.caption("🚀 A SQL query generator powered by Gemini")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if reset_chat:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
        st.rerun()  # Rerun to apply the reset chat immediately

    if prompt := st.chat_input(placeholder="Ask your query here :)"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        with st.spinner(text="Generating response"):
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
                st.chat_message("assistant").write(msg)
        
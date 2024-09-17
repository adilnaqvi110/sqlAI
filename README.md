# SQL AI Query Generator

## Overview

The **SQL AI Query Generator** is a web application designed to help users generate SQL queries using natural language. Powered by the Google Gemini LLM, this tool allows users to input plain language descriptions of the data they want to query, and it will convert that into valid SQL commands. The app also connects to multiple databases, including MySQL, PostgreSQL, SQLite, AWS DB, and S3, and provides a convenient interface to execute queries directly.

---

## Features

- **Natural Language to SQL Conversion**: Generate SQL queries by typing natural language commands.
- **Multi-Database Support**: Connects to MySQL, PostgreSQL, SQLite, AWS DB, and S3.
- **SQL Execution**: Execute generated SQL queries directly on the connected database.
- **Streamlined UI**: Built with Streamlit for a simple and intuitive user interface.
- **User Authentication**: API key-based authentication to access Google Gemini LLM for generating queries.
- **Django Backend**: Handles the logic and database connections.

---

## Technologies Used

- **Backend**: Django
- **Frontend**: Streamlit
- **AI Model**: Google Gemini LLM
- **Databases Supported**: MySQL, PostgreSQL, SQLite3, AWS DB, S3
- **Languages**: Python
- **Authentication**: API Key Integration
- **Web Hosting**: Localhost (or optional deployment)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sql-ai-query-generator.git
2. Run the app:
   ```bash
   streamlit run main.py

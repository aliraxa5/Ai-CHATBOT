import streamlit as st
import sys
import os

# Ensure the backend folder is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import chatbot function from backend
from backend.chatbot import chatbot_response

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Streamlit UI
st.title("🤖 AI Chatbot with LangChain")
st.subheader("Ask me anything!")

# Display chat history (each prompt followed by a response)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input field at the bottom
user_input = st.chat_input("Type your message...")

if user_input:
    # Display the user message immediately
    with st.chat_message("user"):
        st.markdown(user_input)

    # Store user input in session history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get AI response
    response = chatbot_response(user_input)

    # Display AI response immediately
    with st.chat_message("assistant"):
        st.markdown(response)

    # Store AI response in session history
    st.session_state.messages.append({"role": "assistant", "content": response})

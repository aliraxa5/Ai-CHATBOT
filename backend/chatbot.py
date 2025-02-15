import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize AI model
llm = ChatOpenAI(model_name="gpt-4", openai_api_key=OPENAI_API_KEY)

# Add memory for context retention
memory = ConversationBufferMemory()

# Chatbot Function
def chatbot_response(user_input):
    global memory
    conversation = ConversationChain(llm=llm, memory=memory)
    return conversation.predict(input=user_input)

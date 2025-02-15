# Ai-CHATBOT
This repository contains an AI-powered chatbot built using LangChain, designed for conversational AI, knowledge retrieval, and intelligent response generation. The chatbot leverages LLMs (Large Language Models) and integrates seamlessly with various data sources to provide accurate, contextual, and interactive conversations.

# 🤖 AI Chatbot with LangChain

This is an AI-powered chatbot built using **OpenAI's GPT-4**, **LangChain**, and **Streamlit**.

---

## 🛠️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
cd AI_Chatbot
```

### 2️⃣ Create & Activate Virtual Environment
#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install --upgrade pip
pip install openai langchain langchain-community llama-index streamlit python-dotenv
```

### 4️⃣ Set Up OpenAI API Key
Create a **.env** file in the project root and add:
```ini
OPENAI_API_KEY="your-api-key-here"
```

---

## ▶️ Running the Chatbot
After setup, start the chatbot using:
```bash
streamlit run frontend/app.py
```
This will open the chatbot in your browser at `http://localhost:8501`.

---

## 📂 Project Structure
```
📁 AI_Chatbot
│── 📂 backend/          # Chatbot logic
│   │── __init__.py
│   │── chatbot.py
│── 📂 frontend/         # Streamlit UI
│   │── app.py
│── .env                 # API Key (not pushed to GitHub)
│── requirements.txt      # Dependencies
│── README.md            # Project Documentation
```

---

### 🎉 Happy Coding! 🚀


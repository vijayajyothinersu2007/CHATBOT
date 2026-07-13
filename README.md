# 🤖 AI Chatbot using Flask & Google Gemini API

An AI-powered chatbot built with **Python**, **Flask**, and the **Google Gemini API**. This chatbot provides intelligent conversational responses through a simple and responsive web interface.

---

## 📌 Features

- 💬 Real-time AI conversations
- 🤖 Powered by Google Gemini API
- 🌐 User-friendly web interface
- ⚡ Fast response generation
- 🔒 Secure API key management using `.env`
- 📱 Responsive design

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- LangChain
- Google Gemini API

### Frontend
- HTML
- CSS
- JavaScript

### Database
- SQLite

---

## 📂 Project Structure

```
AI-Chatbot/
│
├── app.py
├── config.py
├── database.py
├── requirements.txt
├── README.md
├── .env
│
├── routes/
│   ├── chat_routes.py
│   └── history_routes.py
│
├── services/
│   ├── ai_service.py
│   └── storage_service.py
│
├── database/
│   └── chatbot.db
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
└── templates/
    └── index.html
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/CHATBOT.git
```

### 2. Navigate to the project

```bash
cd CHATBOT
```

### 3. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your own API key.

---

## ▶️ Run the Project

```bash
python app.py
```

The application will start at:

```
http://127.0.0.1:5000
```

Open the URL in your browser.

---

## 📸 Screenshots

Add screenshots of your chatbot interface here.

Example:

```
screenshots/home.png
screenshots/chat.png
```

---

## 📋 Requirements

- Python 3.10 or above
- Flask
- LangChain
- langchain-google-genai
- python-dotenv
- SQLite

---

## 📦 Install Dependencies

```bash
pip install flask
pip install python-dotenv
pip install langchain
pip install langchain-core
pip install langchain-google-genai
```

or

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Enhancements

- User authentication
- Dark mode
- Voice input
- Voice output
- Chat history management
- Multi-language support
- File upload support

---

## 👨‍💻 Author

**Vijaya Jyothi Nersu**

B.Tech CSE (AI & Data Science)

Kakinada Institute of Engineering and Technology for Women





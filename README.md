# 🏥 AI-Driven Public Health Chatbot for Disease Awareness

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-3-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

An intelligent healthcare chatbot that provides disease awareness, symptom checking, preventive healthcare guidance, and emergency detection using NLP techniques.

## 🎯 Project Overview

This is a **portfolio-level project** that demonstrates:
- ✅ AI/NLP implementation in healthcare
- ✅ Backend API development with Flask
- ✅ Database design and management
- ✅ Real-time chat interface
- ✅ Analytics dashboard with data visualization
- ✅ Emergency detection system
- ✅ Social impact technology

## 🌟 Key Features

### 1. 🧠 Intelligent Symptom Checker
- Users describe symptoms → System suggests possible diseases
- Keyword matching with symptom overlap scoring
- Displays match percentage for transparency

### 2. 🚨 Emergency Detection System
- Automatically detects critical keywords (chest pain, breathing problems, etc.)
- Immediate alert with emergency contact numbers
- Logs all emergencies for monitoring

### 3. 📚 Disease Awareness Module
- Comprehensive information on 10+ diseases
- Covers: Causes, Symptoms, Prevention, Risk Factors
- Educational and preventive focus

### 4. 📊 Analytics Dashboard
- Real-time statistics (conversations, emergencies, diseases)
- Interactive charts showing most searched diseases
- Query type distribution visualization
- Chat history and emergency logs

### 5. 💬 Conversational AI
- Natural language processing
- Context-aware responses
- User-friendly interface with example queries

## 🏗️ System Architecture

```
┌─────────────────┐
│   User (Web)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Flask Backend  │
│      API        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  NLP Engine     │
│ (Rule-based +   │
│  Regex)         │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  SQLite DB      │
│  - Diseases     │
│  - Chat Logs    │
│  - Emergencies  │
└─────────────────┘
```

## 🧰 Tech Stack

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with modern animations
- **JavaScript (ES6+)** - Interactive chat functionality
- **Bootstrap 5** - Responsive UI framework
- **Font Awesome** - Icons
- **Chart.js** - Data visualization

### Backend
- **Python 3.8+** - Core language
- **Flask 3.0** - Web framework
- **SQLite3** - Database

### NLP/AI
- **Regex** - Pattern matching
- **Rule-based NLP** - Keyword extraction and matching
- **Text preprocessing** - Tokenization and normalization

## 📁 Project Structure

```
public-health-chatbot/
│
├── app.py                      # Main Flask application
├── init_database.py            # Database initialization script
├── database.db                 # SQLite database (auto-created)
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── templates/
│   ├── index.html             # Main chat interface
│   └── dashboard.html         # Analytics dashboard
│
└── static/
    ├── css/
    │   └── style.css          # Custom styles
    └── js/
        └── chat.js            # Chat functionality
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser

### Step 1: Clone or Download Project

```bash
cd public-health-chatbot
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Initialize Database

```bash
python init_database.py
```

You should see: `✅ Database initialized successfully with 10 diseases!`

### Step 5: Run the Application

```bash
python app.py
```

The application will start at: `http://localhost:5000`

### Step 6: Access the Application

- **Chat Interface**: http://localhost:5000
- **Dashboard**: http://localhost:5000/dashboard

## 📖 Usage Guide

### For Users

1. **Get Disease Information**
   - Type: "Tell me about COVID-19"
   - Type: "What is diabetes"

2. **Check Symptoms**
   - Type: "I have fever and cough"
   - Type: "symptoms like headache and fatigue"

3. **Prevention Tips**
   - Type: "Prevention of dengue"
   - Type: "How to prevent diabetes"

4. **Emergency**
   - Type critical keywords → Automatic emergency alert

### Example Queries

```
✅ "Tell me about Dengue"
✅ "I have chest pain and breathing problem"
✅ "Prevention of malaria"
✅ "What is tuberculosis"
✅ "I'm feeling feverish with body aches"
```

## 🗄️ Database Schema

### Diseases Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary Key |
| name | TEXT | Disease name |
| symptoms | TEXT | Comma-separated symptoms |
| prevention | TEXT | Prevention measures |
| causes | TEXT | Disease causes |
| risk_factors | TEXT | Risk factors |
| info | TEXT | General information |

### Chat Logs Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary Key |
| user_message | TEXT | User's message |
| bot_response | TEXT | Bot's response |
| timestamp | DATETIME | Message timestamp |

### Emergency Logs Table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary Key |
| message | TEXT | Emergency message |
| timestamp | DATETIME | Alert timestamp |

## 🎨 Features Breakdown

### NLP Engine Logic

The chatbot uses multiple NLP techniques:

1. **Text Preprocessing**
   - Lowercasing
   - Special character removal
   - Tokenization

2. **Pattern Matching**
   - Regex patterns for query types
   - Keyword extraction

3. **Symptom Matching Algorithm**
   ```python
   Match Score = (Matched Symptoms / Total User Symptoms) × 100
   ```

4. **Emergency Detection**
   - Keyword list matching
   - Immediate alert triggering

## 📊 API Endpoints

### POST /api/chat
Send a message to the chatbot

**Request:**
```json
{
  "message": "Tell me about COVID-19"
}
```

**Response:**
```json
{
  "type": "disease_info",
  "message": "Disease information...",
  "disease": { ... }
}
```

### GET /api/diseases
Fetch all diseases from database

**Response:**
```json
[
  {
    "id": 1,
    "name": "COVID-19",
    "symptoms": "fever, cough...",
    ...
  }
]
```

### GET /api/stats
Get dashboard statistics

**Response:**
```json
{
  "total_chats": 42,
  "total_emergencies": 2,
  "total_diseases": 10,
  "recent_chats": [...],
  "emergency_logs": [...],
  "top_diseases": [["COVID-19", 15], ...]
}
```

## 🚀 Deployment Options

### Option 1: PythonAnywhere (Free)

1. Upload project files
2. Create virtual environment
3. Configure WSGI file
4. Set working directory

### Option 2: Heroku

1. Create `Procfile`:
   ```
   web: python app.py
   ```

2. Deploy:
   ```bash
   git init
   heroku create
   git push heroku main
   ```

### Option 3: Render

1. Connect GitHub repository
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `python app.py`

## 🎯 Resume Description

Use this for your resume:

> **AI-Driven Public Health Chatbot** | Python, Flask, NLP, SQLite, Bootstrap
> 
> Developed an intelligent healthcare chatbot providing disease awareness, symptom checking, and emergency detection using NLP techniques. Implemented rule-based AI engine with pattern matching, designed SQLite database schema for 10+ diseases, and built interactive analytics dashboard with Chart.js. Features include real-time symptom analysis, automatic emergency alerts, and preventive healthcare guidance. Deployed full-stack application with responsive UI and RESTful API architecture.

## 🔮 Future Enhancements

- [ ] Machine Learning model (Naive Bayes classifier)
- [ ] Multi-language support
- [ ] Voice interaction
- [ ] User authentication
- [ ] Appointment booking integration
- [ ] Push notifications for health tips
- [ ] Mobile app (React Native)
- [ ] Integration with health APIs

## 🤝 Contributing

This is a portfolio project, but suggestions are welcome!

## ⚠️ Disclaimer

**This chatbot is for educational and awareness purposes only.**

- NOT a substitute for professional medical advice
- NOT a diagnostic tool
- Always consult healthcare professionals for medical concerns
- In emergencies, call local emergency services immediately

## 📝 License

MIT License - Feel free to use for learning and portfolio purposes.

## 👨‍💻 Author

Created as a portfolio project demonstrating:
- Backend development
- AI/NLP implementation
- Full-stack web development
- Healthcare technology
- Social impact coding

## 📞 Emergency Numbers

- **India**: 112 / 108
- **USA**: 911
- **UK**: 999
- **Australia**: 000

---

**Built with ❤️ for public health awareness**

## 🎓 Learning Outcomes

By building this project, you'll learn:
- Flask web framework fundamentals
- Database design and SQL operations
- NLP and pattern matching techniques
- RESTful API development
- Frontend-backend integration
- Data visualization with Chart.js
- Git version control
- Project documentation

---

**Questions or Issues?**
This is a self-contained project designed for portfolio use. Customize and extend as needed!

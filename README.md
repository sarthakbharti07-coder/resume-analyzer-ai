# 🧠 AI Career Copilot

An AI-powered resume analyzer built with Flask that gives brutally honest feedback on your resume and helps you plan your career path.

## ✨ Features

- 📄 Upload resume as PDF, DOCX, or paste text
- 🎯 Target-role based analysis
- ⭐ Resume rating out of 10
- ✅ Pros & cons specific to your resume
- 🗺️ Personalized improvement roadmap
- 💼 Realistic career options based on current skills
- 📊 Analysis history saved per user
- 🔐 User authentication (signup/login)

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| AI | Groq API (Llama 3.3 70B) |
| Database | TiDB Cloud (MySQL) |
| ORM | SQLAlchemy |
| Frontend | HTML, CSS, Jinja2 |
| File Parsing | PyPDF2, python-docx |

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Groq API key (free at [console.groq.com](https://console.groq.com))
- TiDB Cloud account (free at [tidbcloud.com](https://tidbcloud.com))

### Installation

1. Clone the repo
```bash
   git clone https://github.com/yourusername/ai-career-copilot.git
   cd ai-career-copilot
```

2. Create and activate virtual environment
```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
```

3. Install dependencies
```bash
   pip install -r requirements.txt
```

4. Set up environment variables — create a `.env` file:

5. Run the app
```bash
   python app.py
```

6. Open `http://127.0.0.1:5000`

## 📸 Screenshots

<!-- Add screenshots here after taking them -->

## 🔮 Future Plans

- [ ] Password hashing
- [ ] Export analysis as PDF
- [ ] LinkedIn profile analyzer
- [ ] Email report delivery
- [ ] Dark mode

## 👤 Author

**Sarthak Bharti**  
[GitHub](https://github.com/yourusername) • [LinkedIn](https://linkedin.com/in/yourprofile)

## 📄 License

MIT License

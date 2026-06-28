# 🧠 Resume Analyzer AI

An AI-powered resume analyzer built with Flask, Groq (LLaMA 3), and TiDB Cloud.
Upload your resume (PDF/DOCX), enter your target job role, and get instant AI feedback instantly.

---
## ✨ Features

- 📄 Upload resume in PDF or DOCX format
- 🎯 Enter your target job role
- 🤖 AI analyzes your resume and returns:
  - ⭐ Overall rating (out of 10)
  - ✅ Pros and cons
  - 📈 Improvement steps
  - 💼 Career options
  - 📝 Summary verdict

---
## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| AI Model | LLaMA 3 via Groq API |
| Database | TiDB Cloud (MySQL) |
| File Parsing | pdfplumber, python-docx |
| ORM | SQLAlchemy |

---
## ✅ Prerequisites

Make sure you have these installed before starting:

- Python 3.10 or above → https://www.python.org/downloads/
- Git → https://git-scm.com/download/win
- A free Groq API key → https://console.groq.com/keys
- A TiDB Cloud account → https://tidbcloud.com

---
## ⚙️ Setup Instructions

### Step 1 — Clone the repository
```bash
git clone https://github.com/sarthakbharti07-coder/resume-analyzer-ai.git
cd resume-analyzer-ai
```
### Step 2 — Create a virtual environment
```bash
python -m venv venv
```
Activate it:

**Windows:**
```bash
venv\Scripts\activate
```
**Mac/Linux:**
```bash
source venv/bin/activate
```
You should see `(venv)` appear in your terminal.

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Create the `.env` file

In the root of the project (same folder as `app.py`), create a file named `.env`:

**Windows:**
```powershell
Set-Content -Path ".env" -Value ""
code .env
```

**Mac/Linux:**
```bash
touch .env
```

Paste the following inside `.env`:

GROQ_API_KEY=your_groq_api_key_here
DATABASE_URL=mysql+pymysql://username:password@host:4000/dbname


**How to get these values:**

- `GROQ_API_KEY` → Go to https://console.groq.com/keys → Create API Key → Copy it
- `DATABASE_URL` → Go to TiDB Cloud → Your Cluster → Connect → Copy the connection string
  - Format: `mysql+pymysql://username:password@host:4000/database_name`

> ⚠️ Never share your `.env` file or commit it to GitHub!

### Step 5 — Run the app
```bash
python app.py
```

### Step 6 — Open in your browser
---

## 📁 Project Structure
resume-analyzer-ai/

├── static/            # CSS, JS, images

├── templates/         # HTML templates

├── app.py             # Main Flask app

├── db.py              # Database connection

├── models.py          # Database models

├── resume_ai.py       # AI analysis logic

├── ai.py              # Groq API helper

├── requirements.txt   # Python dependencies

├── .gitignore         # Files to ignore in Git

└── .env               # Your secret keys (never commit this!)
---

## ❗ Common Errors & Fixes

| Error | Fix |
|---|---|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `GROQ_API_KEY` is None | Check your `.env` file exists in the root folder |
| `Expected string or URL object, got None` | Check `DATABASE_URL` in your `.env` file |
| `git: command not found` | Install Git from https://git-scm.com |
| `python: command not found` | Install Python from https://python.org |

---
## 🔒 Security Notes

- Your `.env` file is listed in `.gitignore` — it will never be pushed to GitHub
- Never hardcode API keys directly in your Python files
- Regenerate your API keys if you accidentally expose them
---
## 👨‍💻 Author

**Sarthak Bharti**
GitHub: [@sarthakbharti07-coder](https://github.com/sarthakbharti07-coder)

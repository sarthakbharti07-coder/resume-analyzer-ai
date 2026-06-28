from flask import Flask, render_template, request, redirect, session
from db import Base, engine, sessionlocal
from resume_ai import analyze_resume
import models
import PyPDF2
import docx
import json
from dotenv import load_dotenv
import os

load_dotenv()  # add this right after imports

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

Base.metadata.create_all(engine)


# home
@app.route("/")
def home():
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/login")


# sign-up
@app.route("/signup", methods=["GET", "POST"])
def signup():
    db = sessionlocal()

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = db.query(models.User).filter_by(email=email).first()

        if existing_user:
            return "User already exists"

        user = models.User(email=email, password=password)
        db.add(user)
        db.commit()

        return redirect("/login")

    return render_template("signup.html")


# login
@app.route("/login", methods=["GET", "POST"])
def login():
    db = sessionlocal()

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = db.query(models.User).filter_by(email=email, password=password).first()

        if user:
            session["user"] = user.email
            return redirect("/dashboard")
        else:
            return "Invalid credentials"

    return render_template("login.html")


# Dashboard
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/login")

    result = None

    if request.method == "POST":
        user_goal = request.form.get("role")
        resume_text = request.form.get("resume")
        file = request.files.get("file")

        # file handling
        if file and file.filename != "":
            if file.filename.endswith(".pdf"):
                try:
                    pdf_reader = PyPDF2.PdfReader(file)
                    text = ""
                    for page in pdf_reader.pages:
                        text += page.extract_text()
                    resume_text = text
                except Exception as e:
                    return f"Error reading PDF: {str(e)}"

            elif file.filename.endswith(".docx"):
                try:
                    doc = docx.Document(file)
                    text = ""
                    for para in doc.paragraphs:
                        text += para.text + "\n"
                    resume_text = text
                except Exception as e:
                    result = {"error": f"Docx error {str(e)}"}

        # validation
        if not user_goal:
            result = {"error": "Please enter a target role."}
        elif not resume_text or resume_text.strip() == "":
            result = {"error": "Please enter your resume text or upload a file."}
        else:
            try:
                result = analyze_resume(resume_text, user_goal)

                # save to database
                db = sessionlocal()
                user = db.query(models.User).filter_by(email=session["user"]).first()
                report = models.reports(
                    users_id=user.id,
                    resume_text=resume_text,
                    result=json.dumps(result),
                )
                db.add(report)
                db.commit()

            except Exception as e:
                result = {"error": f"AI error: {str(e)}"}

    return render_template("dashboard.html", user=session["user"], result=result)


@app.route("/history")
def history():
    if "user" not in session:
        return redirect("/login")

    db = sessionlocal()

    user = db.query(models.User).filter_by(email=session["user"]).first()
    reports = db.query(models.reports).filter_by(users_id=user.id).all()

    # convert json string → dict
    parsed_reports = []
    for r in reports:
        try:
            parsed_result = json.loads(r.result)
        except:
            parsed_result = []

        parsed_reports.append({"resume": r.resume_text, "result": parsed_result})

    return render_template("history.html", reports=parsed_reports)


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)

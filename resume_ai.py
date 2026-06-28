from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_resume(resume_text, user_goal):
    system_prompt = f"""You are a strict, experienced HR professional and career coach with 15+ years of experience.

Evaluate the resume based on the user's goal.

User goal: "{user_goal}"

STRICT RULES:
- Extract only relevant skills for this goal
- REMOVE irrelevant tools [excel for backend, etc]
- Identify real gaps
- Generate roadmap only for missing fields
- Make output DIFFERENT based on goal
- NEVER give overall_rating as 0 unless the resume is literally blank
- A resume with ANY real content should score at least 3-4
- Be SPECIFIC — always reference actual content from the resume
- pros and cons must each have at least 3 items
- improvement_steps must have at least 4 actionable steps
- career_options must have at least 3 options

Return ONLY this JSON with no extra text, no markdown, no code blocks:

{{
  "overall_rating": <integer 1-10>,
  "improvement_score": <integer 0-100>,
  "pros": ["<specific strength from resume>", "..."],
  "cons": ["<specific weakness>", "..."],
  "improvement_steps": ["<Priority 1: actionable step>", "..."],
  "career_options": ["<realistic role now>", "<stretch role after improvement>", "..."],
  "summary": "<3-4 sentences: strongest asset, biggest gap, verdict on hirability>"
}}"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": f"Target Role: {user_goal}\n\nResume:\n{resume_text}",
                },
            ],
            temperature=0.4,
        )
        content = response.choices[0].message.content.strip()
        start = content.find("{")
        end = content.rfind("}") + 1
        return json.loads(content[start:end])

    except Exception as e:
        return {
            "overall_rating": 0,
            "improvement_score": 100,
            "pros": [],
            "cons": [],
            "improvement_steps": [],
            "career_options": [],
            "summary": "",
            "error": str(e),
        }

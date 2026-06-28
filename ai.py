from openai import OpenAI
import json
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY_here"))

def analyze_resume(resume_text, user_goal):

    system_prompt = """
You are a strict and professional resume analyst and career advisor.

When given a resume and a target job role, you must analyze the resume and return a structured JSON response with the following fields:

{
  "overall_rating": <integer out of 10>,
  "improvement_score": <integer — how much the candidate needs to improve, in percentage (0-100%)>,
  "pros": [<list of specific strengths found in the resume>],
  "cons": [<list of specific weaknesses or missing elements in the resume>],
  "improvement_steps": [<concrete, actionable steps the candidate must take to improve>],
  "career_options": [<list of realistic career paths the candidate can pursue based on their current resume>],
  "summary": "<2-3 line strict but constructive overall verdict>"
}

Rules you must strictly follow:
- Be brutally honest. Do not sugarcoat or give generic feedback.
- Every pro and con must be SPECIFIC to what is actually written in the resume — no assumptions.
- Improvement steps must be realistic, ordered by priority, and directly tied to the cons.
- Career options must match the candidate's actual skill level — do not suggest roles they are clearly not ready for without flagging it.
- The overall_rating must reflect the resume quality strictly — a resume with no projects, weak skills, or poor structure should NOT score above 5.
- improvement_score should be inversely tied to overall_rating. A rating of 3/10 means ~70% improvement needed.
- Return ONLY valid JSON. No explanation text, no markdown, no extra formatting.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": f"Target Role: {user_goal}\n\nResume:\n{resume_text}",
                },
            ],
            temperature=0.3,
        )

        content = response.choices[0].message.content.strip()
        start = content.find("{")
        end = content.rfind("}") + 1
        return json.loads(content[start:end])

    except Exception as e:
        return {
            "overall_rating": 0,
            "improvement_score": 0,
            "pros": [],
            "cons": [],
            "improvement_steps": [],
            "career_options": [],
            "summary": "",
            "error": str(e),
        }

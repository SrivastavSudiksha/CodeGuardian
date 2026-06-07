from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_review(file_name, code_diff):
    prompt = f"""
Review the code as a Senior developer.
File: {file_name}
Changes:
{code_diff}

Find issues:
🔴 CRITICAL / 🟡 WARNING / 🟢 SUGGESTION
- Line: [line number]
- Issue: [what is wrong]
- Fix: [how to fix]
"""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text
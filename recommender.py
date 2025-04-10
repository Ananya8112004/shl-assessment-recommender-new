import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Check if API key was loaded
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please check your .env or secrets.toml file.")

# Setup Gemini API
genai.configure(api_key=api_key)

# ✅ Correct model name
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Load SHL data from CSV
def load_shl_data():
    return pd.read_csv("shl_data.csv")

# Generate recommendations using Gemini
def get_recommendations(user_query, df):
    prompt = f"""
You are an SHL assessment assistant.
Given this list of assessments: {df.to_dict(orient='records')}

Recommend up to 10 relevant assessments based on this job query: "{user_query}".

For each result, include:
- Assessment name as clickable link
- Remote support: Yes/No
- Adaptive support: Yes/No
- Duration
- Test type

Format the response as a markdown table.
"""
    response = model.generate_content(prompt)
    return response.text

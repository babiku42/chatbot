import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_bot_response(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful health assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

def get_triage_level(symptoms):
    prompt = f"Classify the urgency of these symptoms: {symptoms}. Answer with: low, medium, or high."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Classify health symptoms into triage urgency levels."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip().lower()

def run_symptom_checker(symptoms):
    prompt = f"The user reports: {symptoms}. What might be the cause? Should they see a doctor?"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a medical assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

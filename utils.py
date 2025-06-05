import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Use your GitHub personal access token saved as env variable GITHUB_TOKEN
token = st.secrets["OPENAI_TOKEN"]
if not token:
    raise ValueError("OPENAI_TOKEN environment variable is not set.")

# Custom GitHub OpenAI-compatible API endpoint and model name
endpoint = "https://models.github.ai/inference"
model_name = "openai/gpt-4.1"  # Changed to available model

# Initialize OpenAI client with custom base URL and API key
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

def get_bot_response(user_input: str) -> str:
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful health assistant."},
            {"role": "user", "content": user_input}
        ],
    )
    return response.choices[0].message.content

def get_triage_level(symptoms: str) -> str:
    prompt = f"Classify the urgency of these symptoms: {symptoms}. Answer with one of these: low, medium, or high."
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "Classify health symptoms into triage urgency levels."},
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content.strip().lower()

def run_symptom_checker(symptoms: str) -> str:
    prompt = f"The user reports these symptoms: {symptoms}. What could be the possible cause(s)? Should they see a doctor?"
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a medical assistant."},
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content

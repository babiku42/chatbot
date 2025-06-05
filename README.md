# 🩺 Health Chatbot with Generative AI

A simple Streamlit app using OpenAI GPT-3.5 to:

- Chat about health topics
- Assess symptom urgency (low/medium/high)
- Suggest possible causes

> ⚠️ Not for medical diagnosis — for informational purposes only.

## Features

- Chatbot powered by OpenAI GPT-3.5
- Triage urgency classification
- Symptom checker module

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/health-chatbot.git
cd health-chatbot
pip install -r requirements.txt
echo "OPENAI_TOKEN=sk-..." > .env
streamlit run app.py

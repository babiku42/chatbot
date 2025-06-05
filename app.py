import streamlit as st
from utils import get_bot_response, get_triage_level, run_symptom_checker

st.set_page_config(page_title="Health AI Assistant", page_icon="🩺")
st.title("🩺 Health Chatbot with AI")

with st.expander("ℹ️ How it works"):
    st.markdown("""
    This chatbot uses OpenAI's GPT model to:
    - Answer health-related questions.
    - Assess urgency of your symptoms.
    - Provide guidance (not a substitute for a doctor).
    """)

user_input = st.text_input("Enter your symptoms or question:")

if st.button("Get Response"):
    if user_input:
        with st.spinner("Thinking..."):
            reply = get_bot_response(user_input)
            triage = get_triage_level(user_input)
            assessment = run_symptom_checker(user_input)

        st.markdown("### 🤖 AI Response")
        st.success(reply)

        st.markdown("### 🚦 Triage Level")
        if "low" in triage:
            st.info("Urgency: **Low** — Monitor your symptoms.")
        elif "medium" in triage:
            st.warning("Urgency: **Medium** — Consider seeing a doctor.")
        elif "high" in triage:
            st.error("Urgency: **High** — Seek medical attention immediately.")
        else:
            st.write(triage)

        st.markdown("### 🩻 Symptom Analysis")
        st.write(assessment)
    else:
        st.warning("Please enter some symptoms or a question.")

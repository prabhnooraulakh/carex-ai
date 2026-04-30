import os
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="CareX AI", page_icon="🩺")

st.title("🩺 CareX AI")
st.markdown("### AI Powered. Human Focused.")

st.warning("⚠️ This is not medical advice. Consult a doctor.")

user_input = st.text_input("Enter your symptoms:")

if user_input:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful healthcare assistant. Give simple advice but always suggest consulting a doctor."},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response.choices[0].message.content
    st.success(reply)

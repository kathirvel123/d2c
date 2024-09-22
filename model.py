
import streamlit as st
import os
from groq import Groq

client = Groq(
    api_key="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",
)
st.title("D2C ChatBot")
st.write("-------")

uploaded_files = st.file_uploader(
    "Load the file to chatbot", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
    st.write("## file has been loaded to the chatbot")
user_input = st.text_input("You: ", "Hello!")

# OpenAI GPT call
def openai_response(prompt):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"{prompt}",
        }
    ],
    model="llama3-8b-8192",
)
    return (chat_completion.choices[0].message.content)

# Display bot response
if user_input:
    response = openai_response(user_input)
    st.write("### Bot: " + response)

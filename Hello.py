import streamlit as st

import os
import openai
from lyzr import QABot
from pprint import pprint
from PIL import Image

# Setup your config
st.set_page_config(
    page_title="Pocket Law",
    layout="wide",  # "wide" or "centered"
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png"
)

# Display an image logo at the top
image = Image.open("lyzr-logo.png")
st.image(image, width=150)

# Display the title of the application
st.title("Lyzr Pocket Law")

# Setting up API Key for OpenAI and environment variable
openai.api_key = st.secrets["apikey"]
os.environ['OPENAI_API_KEY'] = openai.api_key

# Location of the PDF document to be used by the QABot
file_path = '2020-handbook.pdf'

# Text and input box for user to ask their questions
st.text("Ask any law-related question:")
user_question = st.text_input("Your question", "")

# Set a sample question and a button for it
sample_question = "What is traffic law on DUI?"
if st.button('Show Sample Question'):
    user_question = sample_question

#Querry wrapper prompt
prompt = '''Legal Expert: Given your comprehensive understanding of global legal systems, provide a detailed yet concise answer to the following query for educational purposes. This will aid in understanding complex legal principles and their applications. Please include any relevant legal principles, statutes, or case law in your response. Your answer should be informed, authoritative, and as specific as possible to the jurisdiction mentioned (if any).'''

# Initialize the QA Bot with the PDF document
qa_bot = QABot.pdf_qa(input_files=[file_path], system_prompt=prompt)

# Check if the user has input a question or clicked the sample question button
if user_question:
    # Query the model with the question
    response = qa_bot.query(user_question)
    
    # Display the response to the user
    st.text("Answer:")
    st.write(response.response)
else:
    st.write("Please ask a question or click 'Show Sample Question'.")



# Footer or any additional information
with st.expander("ℹ️ - About this App"):
    st.markdown(
        """
    This app uses Lyzr Core to process information. For any inquiries or issues, please contact Lyzr.

    """
    )
    st.link_button("Lyzr", url="https://www.lyzr.ai/", use_container_width=True)
    st.link_button(
        "Book a Demo", url="https://www.lyzr.ai/book-demo/", use_container_width=True
    )
    st.link_button(
        "Discord", url="https://discord.gg/nm7zSyEFA2", use_container_width=True
    )
    st.link_button(
        "Slack",
        url="https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw",
        use_container_width=True,
    )
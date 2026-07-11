import streamlit as st
from dotenv import load_dotenv
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

# -----------------------------
# LLM
# -----------------------------
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=groq_api_key
)

# -----------------------------
# Prompt
# -----------------------------
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a professional translator and summarizer.

Your tasks:

1. Translate the user's text from {from_language} to {to_language}.

2. After translating, create a summary of the translated text in exactly 3 bullet points.

Format your response exactly like this:

### Translation
<translated text>

### Summary
• Bullet 1
• Bullet 2
• Bullet 3
"""
    ),
    ("user", "{text}")
])

parser = StrOutputParser()

chain = prompt | model | parser

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Translator & Summarizer",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("🌍 AI Translator & Summarizer")
st.markdown(
    "Translate any text into another language and automatically generate a concise summary using **LangChain + Groq Llama 3.3 70B**."
)

st.divider()

# -----------------------------
# Languages
# -----------------------------
languages = [
    "English",
    "Arabic",
    "French",
    "German",
    "Spanish",
    "Italian",
    "Chinese",
    "Japanese",
    "Korean",
    "Turkish",
    "Russian",
    "Portuguese",
    "Hindi"
]

col1, col2 = st.columns(2)

with col1:
    from_language = st.selectbox(
        "Translate From",
        languages,
        index=0
    )

with col2:
    to_language = st.selectbox(
        "Translate To",
        languages,
        index=1
    )

# -----------------------------
# Input Text
# -----------------------------
text = st.text_area(
    "Enter your text",
    height=220,
    placeholder="Paste your text here..."
)

# -----------------------------
# Button
# -----------------------------
if st.button("🚀 Translate & Summarize", use_container_width=True):

    if not text.strip():
        st.warning("Please enter some text.")
        st.stop()

    with st.spinner("Generating response..."):

        result = chain.invoke({
            "from_language": from_language,
            "to_language": to_language,
            "text": text
        })

    st.success("Done!")

    st.divider()

    st.markdown(result)

# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
    "Built with ❤️ using Streamlit • LangChain • Groq • Llama 3.3 70B"
)
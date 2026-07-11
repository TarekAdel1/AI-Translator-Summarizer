from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
from dotenv import load_dotenv
import os

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=groq_api_key
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a professional translator and summarizer.

Your tasks:

1. Translate the user's text from {from_language} to {to_language}.

2. Create a SHORT summary of the translated text.

Rules:
- The summary MUST contain exactly 3 bullet points.
- Each bullet point must be ONE sentence only.
- Each bullet point must contain at most 15 words.
- Keep only the most important ideas.
- Do NOT repeat details or examples.
- Respond in the target language.

Format:

### Translation
<translated text>

### Summary
• ...
• ...
• ...
"""
    ),
    ("user", "{text}")
])

parser = StrOutputParser()

chain = prompt | model | parser

app = FastAPI()

add_routes(app, chain, path="/chain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.3", port=7000)


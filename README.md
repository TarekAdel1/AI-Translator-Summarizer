# 🌐 AI Translator & Summarizer

An AI-powered translation and summarization application built with **Python, LangChain, and Groq**.

The project demonstrates how to build an LLM pipeline that takes text in one language, translates it into a target language, and generates a concise **3-point summary** of the translated content.

## 🚀 Features

* 🌍 Translate text between different languages
* 📝 Generate a concise summary of the translated text
* 📌 Summary contains exactly **3 bullet points**
* 🔗 Built using LangChain's prompt and chain abstractions
* ⚡ Powered by Groq for fast LLM inference
* 🔐 API key managed securely using environment variables
* 🎯 Structured prompts for consistent output formatting

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **LangChain Groq**
* **Groq API**
* **Llama 3.3 70B Versatile**
* **python-dotenv**

## 🧠 How It Works

The application follows a simple LLM pipeline:

```text
User Input
    ↓
ChatPromptTemplate
    ↓
Groq LLM
    ↓
Translation + Summarization
    ↓
Formatted Output
```

The prompt dynamically receives:

* Source language
* Target language
* Input text

The LLM then translates the text and generates a short summary containing exactly three bullet points.

## 📋 Example

### Input

```text
Technology has changed the way people live, work, and communicate.
```

**From:** English
**To:** Arabic

### Output

```text
### Translation

تغيرت التكنولوجيا في كيفية حياة الناس، وعملهم، وتواصلهم.

### Summary

• غيرت التكنولوجيا طريقة حياة الناس.
• غيرت التكنولوجيا طريقة عمل الناس.
• غيرت التكنولوجيا طريقة تواصل الناس.
```

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/TarekAdel1/AI-Translator-Summarizer.git
cd AI-Translator-Summarizer
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Groq API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit your `.env` file to GitHub.

Add this to `.gitignore`:

```text
.env
.venv/
__pycache__/
```

## ▶️ Usage

Run the Python script:

```bash
python main.py
```

You can modify the following variables to translate different text:

```python
from_language = "English"
to_language = "Arabic"

text = """
Your text goes here.
"""
```

## 🔗 LangChain Pipeline

The project also demonstrates LangChain's **LCEL (LangChain Expression Language)** for composing the prompt, model, and output parser:

```python
chain = prompt | model | parser

result = chain.invoke({
    "from_language": "English",
    "to_language": "Arabic",
    "text": text
})
```

This creates a simple and reusable LLM pipeline:

```text
Prompt → LLM → Output Parser
```

## 🎯 Project Goals

This project was built to practice:

* Working with LLM APIs
* Using Groq for LLM inference
* Building prompts with LangChain
* Using dynamic prompt variables
* Creating reusable LLM chains
* Controlling LLM output format
* Combining multiple NLP tasks in a single pipeline

## 🔮 Future Improvements

Possible improvements include:

* Add a Streamlit web interface
* Support document/file uploads
* Add automatic language detection
* Add more advanced output parsing
* Support multiple summarization styles
* Add conversation history
* Deploy the application as a web app

## 👨‍💻 Author

**Tarek Adel**

* GitHub: [TarekAdel1](https://github.com/TarekAdel1)
* LinkedIn: [Tarek Adel](https://linkedin.com/in/tarek-adell)

---

⭐ If you found this project useful, consider giving it a star!

# Resume_score
AI Resume Screener lets you upload multiple resumes and match them with a job description using Hugging Face NER and OpenAI embeddings. It extracts skills, ranks candidates by relevance, and displays results in a simple Gradio UI. Built with Python, LangChain, Gradio, and Transformers.
Project Structure:
ai-resume-screener/
│
├── app.py                   # Main Gradio app
├── main.py                 # Core logic runner
├── resume_parser.py        # Extracts raw text and metadata from PDF
├── skill_extractor.py      # Extracts skills using NER
├── utils.py                # Matching logic (optional)
├── example_resume.pdf      # Sample input
├── requirements.txt
└── README.md
# 🧠 AI Resume Screener

Match resumes to job descriptions using **Generative AI + NLP + Transformers**. This tool uses **LangChain**, **Hugging Face models**, and **embeddings** to extract skills from resumes and rank candidates against a job description.

---

## 🔍 Features

- 📄 Extract skills from PDF resumes using LLM-based Named Entity Recognition (NER)
- 💡 Automatically match resumes with job descriptions using semantic embeddings
- 🔎 Highlights matched skills and provides a percentage score
- 🧑‍💻 Simple drag-and-drop UI built with Gradio
- 📋 Supports multiple resume uploads

---

## ⚙️ Tech Stack

- `Python`
- `LangChain`
- `Hugging Face Transformers` (NER using `dslim/bert-base-NER`)
- `PyPDFLoader` (via LangChain)
- `OpenAI Embeddings` (or replaceable with HuggingFace embeddings)
- `Gradio` for UI

---

## 📸 Screenshot

![image](https://github.com/user-attachments/assets/8b6ef705-180b-496b-a41c-36f30ae07722)


---

## 🚀 How It Works

1. 📥 User pastes a job description.
2. 📎 Upload one or more PDF resumes.
3. 📚 Each resume is parsed to extract name, email, phone, and skills.
4. 🤖 Skills are extracted using a pre-trained NER model.
5. 🧠 Resume skills are matched against the job description using vector similarity.
6. ✅ Resumes are ranked with a match score and shown to the user.

---

## 📦 Installation

```bash
git clone https://github.com/<your-username>/ai-resume-screener.git
cd ai-resume-screener

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

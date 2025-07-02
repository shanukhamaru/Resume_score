from langchain_community.document_loaders import PyPDFLoader
import re


def extract_text_from_pdf(pdf_path):
    """
    Extracts all the text from a PDF file using LangChain's PyPDFLoader.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from all pages.
    """
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    # Join the text from all pages
    text = "\n".join(page.page_content for page in pages)
    return text

    

# Sample skill list (can be expanded)
SKILL_KEYWORDS = [
    "python", "java", "sql", "excel", "machine learning", "data analysis", "aws", "c++", "pandas", "numpy"
]

def extract_info_from_text(text):
    """
    Extracts name, email, phone, and skills from resume text.

    Args:
        text (str): Raw resume text.

    Returns:
        dict: Extracted info (name, email, phone, skills)
    """
    # Email
    email = re.search(r"\b[\w\.-]+@[\w\.-]+\.\w+\b", text)
    email = email.group(0) if email else None

    # Phone number (basic match)
    phone = re.search(r"(\+?\d{1,3}[-.\s]?)?\(?\d{2,5}\)?[-.\s]?\d{3,5}[-.\s]?\d{3,5}", text)
    phone = phone.group(0) if phone else None

    # Name (very basic heuristic — usually first line with two words and capitalized)
    lines = text.split("\n")
    name = None
    for line in lines:
        if len(line.split()) == 2 and all(word.istitle() for word in line.split()):
            name = line.strip()
            break



    # Skills
    skills_found = []
    text_lower = text.lower()
    for skill in SKILL_KEYWORDS:
        if skill.lower() in text_lower:
            skills_found.append(skill)

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills_found
    }

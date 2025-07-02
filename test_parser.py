from resume_parser import extract_text_from_pdf, extract_info_from_text

if __name__ == "__main__":
    path = r"C:\Users\shanu\OneDrive\Desktop\ai_resume_screener\sample_data\ShanuKhamaruResume_For_linkedin.pdf"
    text = extract_text_from_pdf(path)
    
    info = extract_info_from_text(text)
    print("Extracted Info:")
    for key, value in info.items():
        print(f"{key}: {value}")

import csv
import json
from resume_parser import extract_text_from_pdf, extract_info_from_text
from skill_extractor import extract_skills

from resume_matcher import compute_similarity

# Step 1: Extract text from the resume PDF
resume_text = extract_text_from_pdf(r"C:\Users\shanu\OneDrive\Desktop\ai_resume_screener\sample_data\ShanuKhamaruResume_For_linkedin.pdf")

# Step 2: Extract basic info (name, email, phone)
basic_info = extract_info_from_text(resume_text)

# Step 3: Extract skills using Hugging Face NER
ner_skills = extract_skills(resume_text)

# Step 4: Combine all data
basic_info["ner_skills"] = ", ".join(ner_skills)
basic_info["skills"] = ", ".join(basic_info["skills"])  # Convert list to comma-separated string

# Step 5a: Display the output
print("\n--- Parsed Resume Information ---")
for key, value in basic_info.items():
    print(f"{key.capitalize()}: {value}")

# Step 5b: Save to JSON
with open("parsed_resume.json", "w") as f:
    json.dump(basic_info, f, indent=2)

# Step 5c: Save to CSV
with open("parsed_resume.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=basic_info.keys())
    writer.writeheader()
    writer.writerow(basic_info)


# Job description (for now you can hardcode it or read from a file)
job_description = """
Looking for a Python developer with experience in machine learning, AWS, and data analysis.
"""

similarity = (compute_similarity(resume_text, job_description)*100)
print("\n--- Resume Match Score ---")
print(f"Similarity with job description: {similarity:.2f} %")

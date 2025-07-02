import gradio as gr
from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from resume_matcher import compute_similarity

def process_resumes(job_description, pdf_files):
    results = []

    for pdf in pdf_files:
        text = extract_text_from_pdf(pdf.name)
        skills = extract_skills(text)
        score = compute_similarity(text, job_description)

        results.append({
            "filename": pdf.name,
            "skills": skills,
            "score": f"{score:.2f}"
        })

    # Format result for display
    output_str = ""
    for res in results:
        output_str += f"📄 **{res['filename']}**\n"
        output_str += f"🔹 Similarity Score: {res['score']}\n"
        #output_str += f"🔸 Extracted Skills: {', '.join(res['skills']) or 'None Found'}\n\n"

    return output_str

interface = gr.Interface(
    fn=process_resumes,
    inputs=[
        gr.Textbox(label="Paste Job Description"),
        gr.File(label="Upload Resume PDFs", file_types=[".pdf"], file_count="multiple")
    ],
    outputs=gr.Markdown(),
    title="AI Resume Screener",
    description="Paste a job description and upload multiple resumes. Get match scores and extracted skills."
)

if __name__ == "__main__":
    interface.launch()

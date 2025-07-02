from sentence_transformers import SentenceTransformer, util

# Load a sentence embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(resume_text, job_description):
    # Generate embeddings
    embeddings = model.encode([resume_text, job_description], convert_to_tensor=True)

    # Calculate cosine similarity
    similarity_score = util.pytorch_cos_sim(embeddings[0], embeddings[1])
    return float(similarity_score)

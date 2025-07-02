from transformers import pipeline

# Load the NER pipeline
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER", grouped_entities=True)

def extract_skills(text):
    entities = ner_pipeline(text)
    skills = []

    for ent in entities:
        if ent["entity_group"] == "MISC":  # Usually MISC or ORG or others depending on model
            skills.append(ent["word"])

    # Remove duplicates and return
    return list(set(skills))

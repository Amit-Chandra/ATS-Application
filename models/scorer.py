import spacy

nlp = spacy.load("en_core_web_sm")

def score_resume(resume_text, required_skills):
    """Scores the resume based on user-provided skills."""
    doc = nlp(resume_text.lower())
    words = set(token.text for token in doc)
    
    required_skills_set = set(skill.lower().strip() for skill in required_skills.split(","))
    score = sum(1 for skill in required_skills_set if skill in words)
    
    return score

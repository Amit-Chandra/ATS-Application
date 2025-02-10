import spacy

nlp = spacy.load("en_core_web_sm")

def score_resume(resume_text, required_skills):
    """
    Scores the resume and provides analysis.
    """
    doc = nlp(resume_text.lower())
    words = set(token.text for token in doc)

    required_skills_set = {skill.lower().strip() for skill in required_skills.split(",")}
    matched_skills = [skill for skill in required_skills_set if skill in words]
    missing_skills = list(required_skills_set - set(matched_skills))

    total_skills = len(required_skills_set)
    score_percentage = (len(matched_skills) / total_skills) * 100 if total_skills > 0 else 0

    analysis = {
        "score": round(score_percentage, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "strongest_section": "Skills/Experience" if matched_skills else "None",
        "weakest_section": "Skills Section" if missing_skills else "None",
    }

    return analysis




















# import spacy

# nlp = spacy.load("en_core_web_sm")

# def score_resume(resume_text, required_skills):
#     """
#     Scores the resume based on user-provided skills and provides a detailed analysis.
    
#     :param resume_text: Extracted text from the resume
#     :param required_skills: Comma-separated user-inputted skills
#     :return: A dictionary containing the percentage score and analysis
#     """
#     doc = nlp(resume_text.lower())
#     words = set(token.text for token in doc)
    
#     # Convert user input skills into a set
#     required_skills_set = {skill.lower().strip() for skill in required_skills.split(",")}

#     # Count matched and missing skills
#     matched_skills = [skill for skill in required_skills_set if skill in words]
#     missing_skills = list(required_skills_set - set(matched_skills))

#     # Calculate percentage score
#     total_skills = len(required_skills_set)
#     score_percentage = (len(matched_skills) / total_skills) * 100 if total_skills > 0 else 0

#     # Identify strongest and weakest areas
#     analysis = {
#         "score": round(score_percentage, 2),
#         "matched_skills": matched_skills,
#         "missing_skills": missing_skills,
#         "strongest_section": "Skills/Experience" if matched_skills else "None",
#         "weakest_section": "Skills Section" if missing_skills else "None",
#     }

#     return analysis

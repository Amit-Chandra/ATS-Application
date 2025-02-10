from flask import Flask, render_template, request
from utils.parser import extract_text_from_pdf
from models.scorer import score_resume

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        job_title = request.form.get("job_title")
        required_skills = request.form.get("required_skills")
        file = request.files.get("resume")

        if not job_title or not required_skills or not file:
            return "All fields are required!", 400
        
        resume_text = extract_text_from_pdf(file)
        score = score_resume(resume_text, required_skills)

        return render_template("result.html", filename=file.filename, score=score, job_title=job_title)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, session
import plotly.graph_objs as go
import json
from utils.parser import extract_text_from_pdf
from models.scorer import score_resume
import plotly
import json


app = Flask(__name__)
app.secret_key = "secret_key"  # Needed for session handling

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        job_title = request.form.get("job_title")
        required_skills = request.form.get("required_skills")
        file = request.files.get("resume")

        if not job_title or not required_skills or not file:
            return "All fields are required!", 400
        
        resume_text = extract_text_from_pdf(file)
        analysis = score_resume(resume_text, required_skills)

        # Store analysis in session for displaying in results
        session["analysis"] = analysis
        session["job_title"] = job_title
        session["filename"] = file.filename

        return redirect(url_for("result"))

    return render_template("index.html")




@app.route("/result")
def result():
    analysis = session.get("analysis", {})
    job_title = session.get("job_title", "Unknown Job")
    filename = session.get("filename", "Unknown File")

    labels = ["Matched Skills", "Missing Skills"]
    values = [len(analysis["matched_skills"]), len(analysis["missing_skills"])]

    pie_chart = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3)])
    pie_chart_json = json.dumps(pie_chart, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template(
        "result.html",
        job_title=job_title,
        filename=filename,
        analysis=analysis,
        pie_chart_json=pie_chart_json
    )



if __name__ == "__main__":
    app.run(debug=True)

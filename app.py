from fastapi import FastAPI
from pydantic import BaseModel

from main import (
    extract_skills,
    read_pdf,
    compare_skills,
    calculate_score
)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Resume Analyzer API"}

class JobRequest(BaseModel):
    job_description: str

@app.post("/analyze")
def analyze(job: JobRequest):
    resume_text = read_pdf("resume.pdf")

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job.job_description)

    matched = resume_skills.intersection(job_skills)

    score = calculate_score(matched, job_skills)

    return {
        "score": round(score, 2),
        "matched_skills": sorted(matched),
        "missing_skills": sorted(job_skills - matched)
    }
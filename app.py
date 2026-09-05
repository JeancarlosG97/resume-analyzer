from fastapi import FastAPI, UploadFile, File, Form
from pypdf import PdfReader
from io import BytesIO

from main import (
    extract_skills,
    calculate_score
)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Resume Analyzer API"}


@app.post("/analyze")
async def analyze(resume: UploadFile = File(...),
                  job_description: str = Form(...)
            ):
    try:
        pdf_bytes = await resume.read()

        reader = PdfReader(BytesIO(pdf_bytes))

        resume_text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                resume_text += page_text

        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_description)
        matched = resume_skills.intersection(job_skills)
        score = calculate_score(matched, job_skills)

        return {
            "score": round(score, 2),
            "matched_skills": sorted(matched),
            "missing_skills": sorted(job_skills - matched)
        }

    except Exception as e:
        return {
            "error": str(e)
        }

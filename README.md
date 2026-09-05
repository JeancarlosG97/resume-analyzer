# Resume Analyzer API

## Overview

Resume Analyzer API is a FastAPI-based backend application that compares a candidate's resume against a job description and generates a compatibility score based on identified technical skills.

The application extracts text from uploaded PDF resumes, identifies software engineering skills using a predefined skills database, compares those skills against the job description, and returns a match score along with matched and missing skills.

---

## Features

- Upload PDF resumes
- Extract text from PDF files
- Analyze job descriptions
- Skill extraction using regex pattern matching
- Support for skill aliases (e.g., GitHub → Git)
- Match score calculation
- Matched skills breakdown
- Missing skills breakdown
- REST API endpoints
- Swagger API documentation

---

## Tech Stack

### Backend

- Python
- FastAPI
- PyPDF
- Regex
- JSON

### Deployment

- Render

---

## API Endpoints

### Home

```http
GET /
```

Response:

```json
{
  "message": "Resume Analyzer API"
}
```

---

### Analyze Resume

```http
POST /analyze
```

#### Request

Multipart Form Data:

| Field | Type |
|---------|---------|
| resume | PDF File |
| job_description | String |

#### Response

```json
{
  "score": 71.43,
  "matched_skills": [
    "java",
    "javascript",
    "react",
    "authentication",
    "cloud"
  ],
  "missing_skills": [
    "python",
    "typescript"
  ]
}
```

---

## How It Works

1. User uploads a PDF resume.
2. Resume text is extracted using PyPDF.
3. User submits a job description.
4. Known skills are loaded from `skills.json`.
5. Regex pattern matching identifies skills in both the resume and job description.
6. Matched skills are calculated.
7. Missing skills are identified.
8. A compatibility score is generated.
9. Results are returned as JSON.

---

## Project Structure

```text
resume-analyzer/
│
├── app.py
├── main.py
├── skills.json
├── requirements.txt
├── README.md
│
└── .venv/
```

### File Descriptions

#### app.py

Contains FastAPI routes and API functionality.

#### main.py

Contains core analysis logic including:

- PDF parsing
- Skill extraction
- Skill comparison
- Score calculation

#### skills.json

Stores known software engineering skills and aliases used during analysis.

#### requirements.txt

Lists Python package dependencies.

---

## Running Locally

### Clone Repository

```bash
git clone <repository-url>
```

### Navigate To Project

```bash
cd resume-analyzer
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Mac/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Application

```bash
uvicorn app:app --reload
```

### Open Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Deployment

The API is deployed on Render.

### Live API

```text
https://resume-analyzer-qog1.onrender.com
```

### Swagger Documentation

```text
https://resume-analyzer-qog1.onrender.com/docs
```

---

## Future Improvements

- DOCX resume support
- ATS-style scoring system
- Expanded skills database
- Skill categories and weighting
- Machine learning based skill extraction
- User authentication
- Resume recommendations

---

## Author

Jeancarlos Guerrero

GitHub:
https://github.com/JeancarlosG97

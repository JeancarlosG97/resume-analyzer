# Resume Analyzer

A Python-based Resume Analyzer that compares a candidate's resume against a job description and calculates a skill match score.

The application extracts text from PDF documents, identifies technical skills from a configurable JSON skill database, compares resume skills against job requirements, and reports matched and missing skills.

---

## Features

✅ Extract text from PDF resumes

✅ Extract text from PDF job descriptions

✅ Load skills from a configurable JSON database

✅ Identify matching skills

✅ Calculate resume-to-job match percentage

✅ Display matched skills

✅ Display missing skills

✅ Easily expand supported skills through JSON

---

## Tech Stack

- Python
- PyPDF
- JSON
- Git / GitHub

---

## Project Structure

```text
resume-analyzer/
│
├── main.py
├── skills.json
├── resume.pdf
├── job.pdf
└── README.md
```

---

## How It Works

### 1. Load Skills

Skills are loaded from `skills.json`.

Example:

```json
{
  "skills": [
    "java",
    "spring boot",
    "sql",
    "aws",
    "docker"
  ]
}
```

---

### 2. Read PDF Files

The analyzer reads:

```text
resume.pdf
job.pdf
```

and extracts the underlying text.

---

### 3. Detect Skills

The application searches both documents for known skills.

Example:

```text
Developed Java applications using Spring Boot and SQL.
```

Detected Skills:

```text
java
spring boot
sql
```

---

### 4. Compare Skills

The application compares:

```text
Resume Skills
```

against

```text
Job Skills
```

using Python set operations.

---

### 5. Calculate Match Score

Formula:

```python
(len(matched_skills) / len(job_skills)) * 100
```

Example:

Resume Skills:

```text
Java
Spring Boot
SQL
```

Job Skills:

```text
Java
Spring Boot
AWS
SQL
```

Output:

```text
Match Score: 75%

Matched Skills:
- Java
- Spring Boot
- SQL

Missing Skills:
- AWS
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/JeancarlosG97/resume-analyzer.git
```

Navigate into the project:

```bash
cd resume-analyzer
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install pypdf
```

---

## Usage

Place:

```text
resume.pdf
job.pdf
```

inside the project directory.

Run the application:

```bash
python main.py
```

Example output:

```text
Matched Score: 42%

Matched Skills:
- Java
- C++
- Git

Missing Skills:
- Python
- Linux
- Bitbucket
- OOAD
```

---

## Current Limitations

- Skill detection currently relies on text matching.
- Similar skills are not automatically treated as equivalent.
- Context-aware matching is not yet implemented.
- No upload interface currently exists.
- No automated career recommendations currently exist.

---

## Planned Improvements

### Phase 1

- Regex-based skill matching
- Improved detection accuracy
- Better handling of skill aliases

### Phase 2

- Error handling for invalid PDFs
- Error handling for missing files
- Improved application reliability

### Phase 3

- FastAPI backend
- Resume uploads
- Job description uploads
- JSON API responses

### Phase 4

- Frontend user interface
- Upload page
- Results page

### Phase 5

- Skill learning recommendations
- Estimated learning hours for missing skills
- Optional AI-powered career guidance

---

## Future Workflow

```text
Upload Resume PDF
          +
Upload Job Description PDF
          ↓
Extract Skills
          ↓
Compare Skills
          ↓
Calculate Match Score
          ↓
Display Missing Skills
          ↓
Recommend Skills To Learn
```

---

## Author

**Jeancarlos Guerrero**

GitHub:

```text
https://github.com/JeancarlosG97
```

LinkedIn:

```text
https://linkedin.com/in/jeancarlosg97
```

---

### Sample Resume Bullet

Built a Python Resume Analyzer that parses PDF resumes and job descriptions, extracts skills from configurable JSON datasets, compares candidate qualifications to job requirements, and generates match scores with missing skill analysis.

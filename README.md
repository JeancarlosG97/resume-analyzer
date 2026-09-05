# Resume Analyzer API

## Overview

FastAPI backend that analyzes uploaded resumes against job descriptions and generates skill match scores.

## Features

- PDF resume upload
- Skill extraction
- Skill matching
- Match score calculation
- Missing skill detection

## API Endpoint

POST /analyze

Inputs:
- Resume PDF
- Job Description

Outputs:
- Score
- Matched Skills
- Missing Skills

## Tech Stack

- Python
- FastAPI
- PyPDF
- Render

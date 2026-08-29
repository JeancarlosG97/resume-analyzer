import json
import re

from pypdf import PdfReader


def extract_skills(text):
    known_skills = load_skills()

    text = text.lower()
    text = " ".join(text.split())

    skills = set()

    for skill, aliases in known_skills.items():

        for alias in aliases:
            if "+" in alias or "#" in alias or "." in alias:
                pattern = re.escape(alias.lower())
            else:
                pattern = rf"\b{re.escape(alias.lower())}\b"

            if re.search(pattern, text):
                skills.add(skill)
                break

    return skills


def read_pdf(file_name):
    reader = PdfReader(file_name)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


def load_skills():
    with open("skills.json", "r") as file:
        return json.load(file)


def compare_skills(resume_skills, job_skills):
    matched = resume_skills.intersection(job_skills)
    missing = job_skills.difference(resume_skills)

    return matched, missing


def calculate_score(matched, job_skills):
    return len(matched) / len(job_skills) * 100


def display_results(score, matched, missing):
    print(f"\nMatched Score: {score:.0f}%")

    print("\nMatched skills:")
    for skill in matched:
        print(skill)

    print("\nMissing Skills:")
    for skill in missing:
        print(skill)


def main():
    resume_text = read_pdf("resume.pdf")
    job_text = read_pdf("job.pdf")

    resume = extract_skills(resume_text)
    job = extract_skills(job_text)

    matched, missing = compare_skills(resume, job)

    score = calculate_score(matched, job)

    display_results(score, matched, missing)


if __name__ == "__main__":
    main()

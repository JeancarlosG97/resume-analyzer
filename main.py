import json


def extract_skills(text):
    known_skills = load_skills()

    text = text.lower()

    skills = set()

    for skill in known_skills:
        if skill in text:
            skills.add(skill)

    return skills


def load_skills():
    with open("skills.json", "r") as file:
        data = json.load(file)

    return set(data["skills"])


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
    with open("resume.txt", "r") as file:
        resume_text = file.read()

    with open("job.txt", "r") as file:
        job_text = file.read()

    resume = extract_skills(resume_text)
    job = extract_skills(job_text)

    matched, missing = compare_skills(resume, job)

    score = calculate_score(matched, job)

    display_results(score, matched, missing)


if __name__ == "__main__":
    main()

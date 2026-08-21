def extract_skills(text):
    skills = set()

    for skill in text.split(","):
        skills.add(skill.strip().lower())

    return skills


def compare_skills(resume_skills, job_skills):
    matched = resume_skills.intersection(job_skills)
    missing = job_skills.difference(resume_skills)

    return matched, missing


def calculate_score(matched, job_skills):
    return len(matched) / len(job_skills) * 100


def display_results(score, matched, missing):
    print(f"\nMatched Score: {score:.0f}%")

    print("\n---Matched skills---")
    for skill in matched:
        print({skill})

    print("\n---Missing Skills---")
    for skill in missing:
        print({skill})


def main():
    resume = extract_skills("Java, Spring Boot, SQL")

    job = extract_skills("Java, AWS, SQL")

    matched, missing = compare_skills(resume, job)

    score = calculate_score(matched, job)

    display_results(score, matched, missing)


if __name__ == "__main__":
    main()
from main import (
    extract_skills,
    compare_skills,
    calculate_score
)

def test_calculate_score_full_match():
    matched = {"java", "spring"}
    job_skills = {"java", "spring"}

    assert calculate_score(matched, job_skills) == 100

def test_calculate_score_partial_match():
    matched = {"java"}
    job_skills = {"java","spring"}

    assert calculate_score(matched, job_skills) == 50

def test_calculate_score_no_match():
    matched = set()
    job_skills = {"java", "spring"}

    assert calculate_score(matched, job_skills) == 0

def test_calculate_score_empty_job_skills():
    assert calculate_score(set(), set()) == 0

def test_compare_skills():
    resume = {"java", "spring"}
    job = {"java", "aws"}

    matched, missing = compare_skills(resume, job)

    assert matched == {"java"}
    assert missing == {"aws"}

def test_extract_skills_basic():
    text = "Java Spring Boot AWS"

    skills = extract_skills(text)

    assert "java" in skills
    assert "spring boot" in skills
    assert "aws" in skills

def test_extract_postgres_alias():
    skills = extract_skills("Experience with postgres")

    assert "postgresql" in skills

def test_extract_cpp():
    skills = extract_skills("Built applications using C++")

    assert "c++" in skills

def test_extract_csharp():
    skills = extract_skills("Developed APIs using C# and ASP.NET")

    assert "c#" in skills
    assert "asp.net" in skills

def test_java_not_detected_inside_javascript():
    skills = extract_skills("javascript")

    assert "java" not in skills

def test_extract_skills_case_insensitive():
    skills = extract_skills("JAVA SPRING BOOT AWS")

    assert "java" in skills
    assert "spring boot" in skills
    assert "aws" in skills

def test_extract_duplicate_skills():
    skills = extract_skills(
        "Java Java Java Spring Boot"
    )

    assert "java" in skills
    assert "spring boot" in skills

    assert len(skills) == 3

def test_extract_github_maps_to_git():
    skills = extract_skills(
        "Used GitHub for version control"
    )

    assert "git" in skills

def test_extract_rest_api_alias():
    skills = extract_skills(
        "Built several RESTful APIs"
    )

    assert "rest api" in skills

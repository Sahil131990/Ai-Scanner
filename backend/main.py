from fastapi import FastAPI
from github_service import clone_repo
from sonar_service import run_sonar_scan
from ai_service import fix_issues
from test_generator import generate_tests

app = FastAPI()

@app.post("/scan")
def scan_repo(repo_url: str, branch: str):

    path = clone_repo(repo_url, branch)

    issues = run_sonar_scan(path)

    fixed_code = fix_issues(issues)

    tests = generate_tests(fixed_code)

    return {
        "issues": issues,
        "fixes": fixed_code,
        "tests": tests
    }
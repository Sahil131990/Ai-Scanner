import git
import shutil
import os

def clone_repo(repo_url, branch):
    repo_path = "./repo"

    if os.path.exists(repo_path):
        shutil.rmtree(repo_path)

    git.Repo.clone_from(repo_url, repo_path, branch=branch)

    return repo_path

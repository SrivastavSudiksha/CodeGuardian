from github import Github
import os
from dotenv import load_dotenv

load_dotenv()
git_work=Github(os.getenv("GITHUB_TOKEN"))

def get_pr_diff(repo_name, pr_number):
    repo=git_work.get_repo(repo_name)
    pr= repo.get_pull(pr_number)

    files=[]
    for file in pr.get_files():
        if file.patch:
            files.append({
                "filename": file.filename,
                "patch": file.patch
                })
    return files
 
def comment(repo_name, pr_number,review_text):
    repo=git_work.get_repo(repo_name)
    pr=repo.get_pull(pr_number)
    pr.create_issue_comment(f"Hi I a CODE REVIWER BOT, made by Sudiksha\n I reviwed  the code and:\n\n {review_text}")

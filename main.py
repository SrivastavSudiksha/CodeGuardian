from fastapi import FastAPI, Request
from dotenv import load_dotenv
from github_utils import get_pr_diff, comment
from llm_review import get_review

load_dotenv()
app = FastAPI()

@app.post("/webhook")
async def handle_webhook(request: Request):
    data = await request.json()
   
    if data.get("action") != "opened":
        return {"status": "ignored"}
    
    repo_name = data["repository"]["full_name"]
    pr_number = data["number"]
    
    print(f"I have recived PR: #{pr_number} from: {repo_name}")
    
    files = get_pr_diff(repo_name, pr_number)
    
    full_review = ""
    for file in files:
        review = get_review(file["filename"], file["patch"])
        full_review += f"### `{file['filename']}`\n{review}\n\n---\n\n"
    

    comment(repo_name, pr_number, full_review)
    print("✅ Review has been posted!")
    
    return {"status": "done"}
import os, json
import requests

def create_pr_comment(pr_number, comment):
    url = f"{os.getenv('GITHUB_API_URL')}/repos/{os.getenv('GITHUB_REPOSITORY')}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"Bearer {os.getenv('GH_TOKEN')}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "body": "Pytest results \n"+"Test Cases"+comment
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response

if __name__ == "__main__":
    pr_number = os.getenv('PR_NUMBER')
    comment = os.getenv('RESULT')
    response = create_pr_comment(pr_number, comment)
    

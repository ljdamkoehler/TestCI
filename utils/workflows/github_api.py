import os
import sys

import requests

class GitHubAPI:
    def __init__(self, pr_number) -> None:
        self.pr_number = pr_number
        self.comments_url = f"{os.environ['GITHUB_API_URL']}/repos/{os.environ['GITHUB_REPOSITORY_OWNER']}/{os.environ['GITHUB_REPOSITORY']}/issues/{self.pr_number}/comments"
        self.headers = {
            "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
            "Content-Type": "application/json"
        }
    
    def post_pr_comment(self, comment_body):
        payload = {
        "body": comment_body
        }
        response = requests.post(self.comments_url, headers=self.headers, json=payload)
        if response.status_code == 201:
            print("Comment posted successfully.")
        else:
            # Exit with a failure code (1) if checklist was not successfully posted.
            print(f"Failed to post comment. Status code: {response.status_code}")
            sys.exit(1)

    def find_pr_comment(self):
        pass
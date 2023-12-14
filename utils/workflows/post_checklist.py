"""
Luke Damkoehler for CCI Systems (12/14/2023): This script 
posts the contents of utils/workflows/pr_checklist.txt as a
comment on a PR. It is meant to be called by a GitHub workflow
job. Needed environmental variables will only be available in 
that environment. This will not work locally. The PR number needs 
to be included as the first script arg when calling this script.
"""

import os
import sys
import requests


def main():
    # Define variables for the rpa-automations GitHub repo.
    # base_url = "https://api.github.com/repos"
    # repo_owner = "ccisystems"
    # repo_name = "rpa-automations"
    base_url = "https://api.github.com/repos"
    repo_owner = "ljdamkoehler"
    repo_name = "TestCI"
    # The PR number needs to be included as the first script arg when calling this script.
    try:
        pr_number = sys.argv[1]
    except Exception as e:
        raise Exception ('The PR number needs to be included as the first script arg when calling this script')
    # Open the text file containing the checklist.
    checklist_file = "utils/workflows/pr_checklist.txt"
    with open(checklist_file, "r") as file:
        checklist = file.read()
    # Post the checklist to the PR via the GitHub API.
    url = f"{base_url}/{repo_owner}/{repo_name}/issues/{pr_number}/comments"
    # 'GITHUB_TOKEN' wil be available in the GitHub Actions environment.
    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
        "Content-Type": "application/json"
    }
    payload = {
        "body": checklist
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        print("Comment posted successfully.")
    else:
        # Exit with a failure code (1) if checklist was not successfully posted.
        print(f"Failed to post comment. Status code: {response.status_code}")
        sys.exit(1)

if __name__ == '__main__':
    main()

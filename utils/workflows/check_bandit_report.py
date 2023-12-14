"""
Luke Damkoehler for CCI Systems (12/14/2023):
"""

import json
import sys
import os
import requests

BLOCKING_SEVERITY_LIST = [
    'MEDIUM',
    'HIGH'
]

def main():
    report_file = 'bandit_report.json'
    with open(report_file, 'r') as report:
        data = json.load(report)
    
    block_pr = False 

    bandit_issue_list = []
    if not data['results']:
        return
    for result in data['results']:
        if result['issue_severity'] in BLOCKING_SEVERITY_LIST:
            block_pr = True
        bandit_issue_tuple = (
            f"Severity: {result['issue_severity']}",
            f"Confidence: {result['issue_confidence']}",
            f"Filename: {result['filename']}",
            f"Line: {result['line_number']}",
            f"Issue: {result['issue_text']}",
            f"Issue Link: {result['issue_cwe']['link']}",
            f"Bandit Link: {result['more_info']}",
            '-----------------------'
        )
        for issue in bandit_issue_tuple:
            bandit_issue_list.append(issue)
    if bandit_issue_list:
        bandit_str = "\n".join(bandit_issue_list)
        pr_str = bandit_str 
        base_url = "https://api.github.com/repos"
        repo_owner = "ljdamkoehler"
        repo_name = "TestCI"
        pr_number = sys.argv[1]
        url = f"{base_url}/{repo_owner}/{repo_name}/issues/{pr_number}/comments"
        headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github.v3+json"
        }
        print(pr_str)
        payload = {
            "body": f"### Bandit Security Issues \n {pr_str}",
            "content_type": "text"
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 201:
            print("Comment posted successfully.")
        else:
            # Exit with a failure code (1) if checklist was not successfully posted.
            print(f"Failed to post comment. Status code: {response.status_code}")
    if block_pr:
        sys.exit(1)

if __name__ == "__main__":
    main()

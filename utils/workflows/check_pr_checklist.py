"""
Luke Damkoehler for CCI Systems (10/30/2023):

"""

import os
import requests
import sys

def main():
    pr_number = sys.argv[1]
   
    response = requests.get(
        f"https://api.github.com/repos/{os.environ['GITHUB_REPOSITORY']}/issues/{pr_number}/comments",
        headers={"Authorization": f"token {os.environ['GITHUB_TOKEN']}"}
    )
    if response.status_code == 200:
        pr_data = response.json()
    else:
        print(f"Failed to fetch PR details: Status code {response.status_code}")
        sys.exit(1)
    
    check_list_comment = None

    for comment in pr_data:
        if '## Code Review Checklist' in comment['body']:
            check_list_comment = comment
            break

    if not check_list_comment:
        sys.exit(1)


    if '- [ ]' in check_list_comment['body']:
        print('Not all code review items are checked!')
        sys.exit(1)

if __name__ == "__main__":
    main()
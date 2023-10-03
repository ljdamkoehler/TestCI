import os
import requests
import sys

def main():
    # Get the PR description
    pr_number = sys.argv[1]
    print(pr_number)
    print(f"https://api.github.com/repos/{os.environ['GITHUB_REPOSITORY']}/pulls/{pr_number}")
    response = requests.get(
        f"https://api.github.com/repos/{os.environ['GITHUB_REPOSITORY']}/pulls/{pr_number}",
        headers={"Authorization": f"token {os.environ['GITHUB_TOKEN']}"}
    )
    if response.status_code == 200:
        pr_data = response.json()
        pr_description = pr_data.get("body", "")
    else:
        print(f"Failed to fetch PR details: Status code {response.status_code}")
    print('Desription +++++++++++++++++++++++++++++++++++')
    print(pr_description)
    # Define the checklist items
    checklist_items = [
        "Code follows coding conventions",
        "Code is well-documented",
        "Code passes all tests",
        "Code is reviewed by at least two developers",
    ]

    # Initialize a list to collect unchecked items
    unchecked_items = []

    # Check if all checklist items are checked
    for item in checklist_items:
        if f"- [ ] {item}" not in pr_description:
            unchecked_items.append(item)

    if not unchecked_items:
        print("All checklist items are checked. PR is ready to merge.")
    else:
        print("Not all checklist items are checked. Please complete the following:")
        for item in unchecked_items:
            print(f"- {item}")
        exit(1)

if __name__ == "__main__":
    main()

import os
requests = __import__('requests')
base_url = "https://api.github.com/repos"
repo_owner = "ljdamkoehler"
repo_name = "TestCI"
pr_number = os.getenv('GITHUB_REF').split('/')[-1]  # Extract PR number from GITHUB_REF
checklist_file = "checklist.txt"

# Read the checklist from the file
with open(checklist_file, "r") as file:
    checklist = file.read()

# Create the comment body
comment_body = checklist

# Create the comment via the GitHub API
url = f"{base_url}/{repo_owner}/{repo_name}/issues/{pr_number}/comments"
headers = {
    "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
    "Content-Type": "application/json"
}
payload = {
    "body": comment_body
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 201:
    print("Comment posted successfully.")
else:
    print(f"Failed to post comment. Status code: {response.status_code}")

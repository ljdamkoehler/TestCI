import os
import json
import requests

def get_modified_python_files():
    event_path = os.environ['GITHUB_EVENT_PATH']
    with open(event_path, 'r') as f:
        event_data = json.load(f)

    pr_url = event_data['pull_request']['url']
    files_url = pr_url + '/files'
    response = requests.get(files_url)
    modified_files = [f['filename'] for f in response.json() if f['filename'].endswith('.py')]
    return modified_files

if __name__ == "__main":
    modified_files = get_modified_python_files()
    with open("modified_files.txt", "w") as file:
        for file_path in modified_files:
            file.write(file_path + "\n")


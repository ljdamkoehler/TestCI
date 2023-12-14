"""
Luke Damkoehler for CCI Systems (10/30/2023):
"""

import os
import json
import requests

def get_modified_python_files():
    event_path = os.environ['GITHUB_EVENT_PATH']
    print(event_path)
    with open(event_path, 'r') as f:
        event_data = json.load(f)

    pr_url = event_data['pull_request']['url']
    files_url = pr_url + '/files'
    print(files_url)
    response = requests.get(files_url)
    print(response.json())
    modified_files = [f['filename'] for f in response.json() if f['filename'].endswith('.py')]
    return modified_files

if __name__ == "__main__":
    modified_files = get_modified_python_files()
    print(" ".join(modified_files))
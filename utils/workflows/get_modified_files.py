"""
Luke Damkoehler for CCI Systems (10/30/2023):
"""

import os
import json
import requests

STATUSES_TO_CHECK = ['added', 'modified']

def get_modified_python_files():
    event_path = os.environ['GITHUB_EVENT_PATH']
    # print('EVENT PATH!!!')
    # print(event_path)
    print('Here!!!!')
    print(os.environ['GITHUB_REF'])
    with open(event_path, 'r') as f:
        event_data = json.load(f)

    pr_url = event_data['pull_request']['url']
    files_url = pr_url + '/files'
    print(files_url)
    response = requests.get(files_url)
    print('THE JSON!!!')
    print(response.json())
    modified_files = [f['filename'] for f in response.json() if f['filename'].endswith('.py') and f['status'] in STATUSES_TO_CHECK]
    return modified_files

if __name__ == "__main__":
    modified_files = get_modified_python_files()
    print(" ".join(modified_files))
"""
Luke Damkoehler for CCI Systems (12/14/2023):
"""

import json
import sys

def main():
    report_file = 'bandit_report.json'
    with open(report_file, 'r') as report:
        data = json.load(report)
        if data['results']:
            print("Bandit issues found:")
            for result in data['results']:
                print(f"Severity: {result['issue_severity']}")
                print(f"Confidence: {result['issue_confidence']}")
                print(f"Filename: {result['filename']}")
                print(f"Line: {result['line_number']}")
                print(f"Test ID: {result['test_id']}")
                print(f"Issue: {result['issue_text']}")
            sys.exit(1)
        else:
            print('No Bandit issues were found!')

if __name__ == "__main__":
    main()

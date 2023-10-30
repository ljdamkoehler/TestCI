import json
import sys

def check_bandit_report(report_file):
    with open(report_file, 'r') as report:
        data = json.load(report)
        print('The report has been opened!!')
        print(data)
        if data['results']:
            print("Bandit issues found:")
            for result in data['results']:
                print(f"Severity: {result['issue_severity']}")
                print(f"Confidence: {result['issue_confidence']}")
                print(f"Filename: {result['filename']}")
                print(f"Line: {result['line_number']}")
                print(f"Test ID: {result['test_id']}")
                print(f"Issue: {result['issue_text']}")
            sys.exit(1)  # Exit with a non-zero status code to indicate failure

if __name__ == "__main__":
    check_bandit_report("bandit_report.json")

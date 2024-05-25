# main.py

from scanner.vulnerability_scanner import scanner
from reporting.report_generator import generate_report

def main(url):
    vulnerabilities = scanner(url)
    generate_report(vulnerabilities)

if __name__ == "__main__":
    url = "https://example.com"
    main(url)
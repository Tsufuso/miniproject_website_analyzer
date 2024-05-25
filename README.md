# Vulnerability Analyzer

## This vulnerability analyzer is a simple tool designed to detect various types of potential attacks on a given website. It includes modules for detecting SQL injections, code injections, XSS (Cross-Site Scripting) attacks, and CSRF (Cross-Site Request Forgery) attacks.

# Features
SQL Injection Detection: Searches for telltale signs of SQL injection in the HTML content of the page.
Code Injection Detection: Analyzes HTML content for malicious script tags.
XSS Attack Detection: Injects XSS payloads into query parameters and checks for execution in the response.
CSRF Attack Detection: Analyzes HTML forms for the presence of CSRF tokens and checks their protection on form submissions.

# Usage
Install Dependencies: Ensure you have Python 3 installed along with the requests and beautifulsoup4 libraries.

# Execution: 
Run the main.py file specifying the target URL to analyze. For example:

# bash
`python main.py https://example.com`

# Vulnerability Report:
 The program will generate an HTML report in the report.html file, listing all detected vulnerabilities.

# Project Structure
```
vulnerability_analyzer/
│
├── scanner/
│   ├── __init__.py
│   └── vulnerability_scanner.py
│
├── reporting/
│   ├── __init__.py
│   ├── assets/
│   │   └── template.html
│   └── report_generator.py
│
├── main.py
│
└── .gitignore
```

# Development and Contributions
If you'd like to contribute to this project, feel free to submit issues, feature requests, or even pull requests. Any contributions are welcome!

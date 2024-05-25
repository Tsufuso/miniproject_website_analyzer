from jinja2 import Template

def generate_report(vulnerabilities):
    with open('reporting/assets/template.html', 'r') as file:
        template_content = file.read()
    template = Template(template_content)
    report_html = template.render(vulnerabilities=vulnerabilities)
    with open('report.html', 'w') as file:
        file.write(report_html)
    print("Le rapport de vulnérabilités a été généré avec succès : report.html")

import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from datetime import datetime

def generate_report(domain):
    output_files = [
        'subdomains.txt',
        'live_hosts.txt',
        'tech_stack.txt',
        'dir_enum_results.txt',
        'param_discovery_results.txt',
        'dns_enum_results.txt',
        'vuln_scan_results.txt',
        'exploit_poc_results.txt'
    ]

    data = {}
    for filename in output_files:
        path = os.path.join('output', filename)
        if os.path.exists(path):
            with open(path, 'r') as f:
                data[filename.replace('.txt', '')] = f.read().splitlines()
        else:
            data[filename.replace('.txt', '')] = ["No data found."]

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report_template.html')

    rendered = template.render(domain=domain, date=datetime.now(), data=data)
    report_html = f'output/{domain}_report.html'
    report_pdf = f'output/{domain}_report.pdf'

    with open(report_html, 'w') as f:
        f.write(rendered)

    HTML(report_html).write_pdf(report_pdf)
    return report_html, report_pdf

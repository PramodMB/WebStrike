from modules.subdomain_enum import run_subdomain_enum
from modules.live_check import live_check_httpx, live_check_httprobe, live_check_custom
from modules.tech_detect import detect_with_whatweb, detect_with_custom
from modules.dir_bruteforce import run_ffuf, run_dirsearch
from modules.param_discovery import run_arjun, run_paramspider
from modules.dns_enum import run_dnsrecon, run_dnsenum
from modules.vuln_scan import run_nuclei, run_nikto, run_wpscan
from modules.exploit_poc import run_dalfox, run_sqlmap, run_open_redirect_check
from modules.report_generator import generate_report
import time


def show_banner():
    print(r"""
██     ██ ███████ ██████  ███████ ██████  ████████ ██████  ██   ██ ███████
██     ██ ██      ██   ██ ██        ██    ██    ██   ██    ██ ██   ██        
██  █  ██ █████   ██████  ███████   ██    ████████   ██    █████   ██████   
██ ███ ██ ██      ██   ██      ██   ██    ██ ██      ██    ██ ██   ██      
 ███ ███  ███████ ██████  ███████   ██    ██   ███ ██████  ██   ██ ███████

                            _
                           /(|
                          (  :
                         __\  \  _____
                       (____)  `|
                      (____)|   |
                       (____).__|
                        (___)__.|_____

             Web Application Security Scanner
                     by Pramod ⚔️
""")


def print_and_display(label, data):
    print(f"\n{label}\n{'-' * len(label)}")
    if data:
        for line in data:
            print(line)
    else:
        print("No data found.")

def get_domain():
    while True:
        domain = input("🔍 Enter the domain (e.g., example.com): ").strip()
        if domain:
            return domain.replace("https://", "").replace("http://", "").split('/')[0]
        print("❌ Invalid input. Please try again.")

def choose_subenum_tools():
    tools_map = {
        '1': 'subfinder',
        '2': 'crtsh',
        '3': 'amass',
        '4': 'assetfinder',
        '0': 'back'
    }

    print("\n🛠️  Choose subdomain tools to use:")
    for k, v in tools_map.items():
        print(f"  [{k}] {v}")

    while True:
        selection = input("👉 Enter comma-separated numbers (e.g., 1,2,3): ").strip()
        selected = [s.strip() for s in selection.split(',')]
        
        if '0' in selected:
            return 'back'
        
        valid = all(s in tools_map and s != '0' for s in selected)
        if valid:
            return [tools_map[s] for s in selected]
        
        print("❌ Invalid choice. Try again.")

def choose_livecheck_tool():
    tools_map = {
        '1': 'httpx',
        '2': 'httprobe',
        '3': 'custom',
        '0': 'back'
    }

    print("\n🌐 Choose live-check tool:")
    for k, v in tools_map.items():
        print(f"  [{k}] {v}")

    while True:
        choice = input("👉 Choose one (e.g., 1): ").strip()
        if choice == '0':
            return 'back'
        if choice in tools_map:
            return tools_map[choice]
        print("❌ Invalid choice. Try again.")

def choose_tech_tool():
    tools_map = {
        '1': 'whatweb',
        '2': 'custom',
        '0': 'back'
    }

    print("\n🧱 Choose technology detection tool:")
    for k, v in tools_map.items():
        print(f"  [{k}] {v}")

    while True:
        choice = input("👉 Choose one (e.g., 1): ").strip()
        if choice == '0':
            return 'back'
        if choice in tools_map:
            return tools_map[choice]
        print("❌ Invalid choice. Try again.")

def choose_dirfuzz_tool():
    tools_map = {
        '1': 'ffuf',
        '2': 'dirsearch',
        '0': 'back'
    }

    print("\n📂 Choose directory brute-force tool:")
    for k, v in tools_map.items():
        print(f"  [{k}] {v}")

    while True:
        choice = input("👉 Choose one (e.g., 1): ").strip()
        if choice == '0':
            return 'back'
        if choice in tools_map:
            return tools_map[choice]
        print("❌ Invalid choice. Try again.")

def choose_param_tool():
    tools_map = {
        '1': 'arjun',
        '2': 'paramspider',
        '0': 'back'
    }

    print("\n🧩 Choose parameter discovery tool:")
    for k, v in tools_map.items():
        print(f"  [{k}] {v}")

    while True:
        choice = input("👉 Choose one (e.g., 1): ").strip()
        if choice == '0':
            return 'back'
        if choice in tools_map:
            return tools_map[choice]
        print("❌ Invalid choice. Try again.")

def choose_dns_tool():
    tools_map = {
        '1': 'dnsrecon',
        '2': 'dnsenum',
        '0': 'back'
    }

    print("\n🌐 Choose DNS enumeration tool:")
    for k, v in tools_map.items():
        print(f"  [{k}] {v}")
        
    while True:
        choice = input("👉 Choose one (e.g., 1): ").strip()
        if choice == '0':
            return 'back'
        if choice in tools_map:
            return tools_map[choice]
        print("❌ Invalid choice. Try again.")

def choose_vuln_tool():
    tools_map = {
        '1': 'nuclei',
        '2': 'nikto',
        '3': 'wpscan',
        '0': 'back'
    }

    print("\n🔥 Choose vulnerability scanning tool:")
    for k, v in tools_map.items():
        print(f"  [{k}] {v}")
        
    while True:
        choice = input("👉 Choose one (e.g., 1): ").strip()
        if choice == '0':
            return 'back'
        if choice in tools_map:
            return tools_map[choice]
        print("❌ Invalid choice. Try again.")

def choose_poc_tool():
    tools_map = {
        '1': 'dalfox',
        '2': 'sqlmap',
        '3': 'openredirect',
        '0': 'back'
    }

    print("\n🧪 Choose exploit PoC tool:")
    for k, v in tools_map.items():
        print(f"  [{k}] {v}")

    while True:
        choice = input("👉 Choose one (e.g., 1): ").strip()
        if choice == '0':
            return 'back'
        if choice in tools_map:
            return tools_map[choice]
        print("❌ Invalid choice. Try again.")

def run_live_check(domains, tool_choice):
    if tool_choice == 'httpx':
        return live_check_httpx(domains)
    elif tool_choice == 'httprobe':
        return live_check_httprobe(domains)
    else:
        return live_check_custom(domains)

def run_tech_detect(urls, tool_choice):
    if tool_choice == 'whatweb':
        return detect_with_whatweb(urls)
    else:
        return detect_with_custom(urls)

def main():
    show_banner()

    while True:
        domain = get_domain()
        tools = choose_subenum_tools()

        if tools == 'back':
            print("🔄 Restarting...\n")
            continue

        print(f"\n[*] Running Subdomain Enumeration on {domain} using: {', '.join(tools)}")
        subdomains = run_subdomain_enum(domain, tools)

        print_and_display("✅ Found Subdomains", subdomains)

        yn = input("\n🔎 Do you want to check which subdomains are live? (y/n): ").strip().lower()
        if yn == 'y':
            live_tool = choose_livecheck_tool()
            if live_tool == 'back':
                continue
            live_hosts = run_live_check(subdomains, live_tool)
            print_and_display("✅ Live Subdomains", live_hosts)
        else:
            live_hosts = []

        yn = input("\n🏗️ Do you want to fingerprint tech stack of live subdomains? (y/n): ").strip().lower()
        if yn == 'y':
            tech_tool = choose_tech_tool()
            if tech_tool == 'back':
                continue
            targets = live_hosts if live_hosts else subdomains
            tech_info = run_tech_detect(targets, tech_tool)
            print_and_display("✅ Tech Stack Info", tech_info)

        yn = input("\n📁 Do you want to brute-force directories/files? (y/n): ").strip().lower()
        if yn == 'y':
            dir_tool = choose_dirfuzz_tool()
            if dir_tool == 'back':
                continue
            wordlist = input("📜 Enter path to wordlist (e.g., wordlists/common.txt): ").strip()
            targets = live_hosts if live_hosts else subdomains

            if dir_tool == 'ffuf':
                results = run_ffuf(targets, wordlist)
            else:
                results = run_dirsearch(targets, wordlist)

            print_and_display("✅ Directory Brute-force Results", results)

        yn = input("\n🧩 Do you want to discover parameters for endpoints? (y/n): ").strip().lower()
        if yn == 'y':
            param_tool = choose_param_tool()
            if param_tool == 'back':
                continue
            targets = live_hosts if live_hosts else subdomains

            if param_tool == 'arjun':
                results = run_arjun(targets)
            else:
                results = run_paramspider(targets)

            print_and_display("✅ Parameter Discovery Results", results)

        yn = input("\n🌐 Do you want to perform DNS enumeration? (y/n): ").strip().lower()
        if yn == 'y':
            dns_tool = choose_dns_tool()
            if dns_tool == 'back':
                continue

            if dns_tool == 'dnsrecon':
                results = run_dnsrecon(domain)
            else:
                results = run_dnsenum(domain)

            print_and_display("✅ DNS Enumeration Results", results)

        yn = input("\n🔥 Do you want to scan for vulnerabilities? (y/n): ").strip().lower()
        if yn == 'y':
            vuln_tool = choose_vuln_tool()
            if vuln_tool == 'back':
                continue
            targets = live_hosts if live_hosts else subdomains

            if vuln_tool == 'nuclei':
                results = run_nuclei(targets)
            elif vuln_tool == 'nikto':
                results = run_nikto(targets)
            else:
                results = run_wpscan(targets)

            print_and_display("✅ Vulnerability Scan Results", results)

        yn = input("\n🧪 Do you want to run exploit PoC checks? (y/n): ").strip().lower()
        if yn == 'y':
            poc_tool = choose_poc_tool()
            if poc_tool == 'back':
                continue
            targets = live_hosts if live_hosts else subdomains

            if poc_tool == 'dalfox':
                results = run_dalfox(targets)
            elif poc_tool == 'sqlmap':
                results = run_sqlmap(targets)
            else:
                results = run_open_redirect_check(targets)

            print_and_display("✅ Exploit PoC Results", results)

        yn = input("\n🧾 Do you want to generate an HTML + PDF report? (y/n): ").strip().lower()
        if yn == 'y':
            html_path, pdf_path = generate_report(domain)
            print(f"\n✅ Report generated: {html_path}\n✅ PDF version: {pdf_path}")

        break


if __name__ == '__main__':
    main()

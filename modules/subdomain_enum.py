import subprocess
import requests

def subfinder_enum(domain):
    print("[*] Running subfinder...")
    try:
        result = subprocess.run(['subfinder', '-d', domain, '-silent'],
                                capture_output=True, text=True)
        return result.stdout.strip().splitlines()
    except Exception as e:
        print(f"[-] Subfinder failed: {e}")
        return []

def crtsh_enum(domain):
    print("[*] Querying crt.sh...")
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url, timeout=10)
        data = response.json()
        subdomains = set()
        for item in data:
            name_value = item.get("name_value")
            if name_value:
                for entry in name_value.split("\n"):
                    if domain in entry:
                        subdomains.add(entry.strip())
        return list(subdomains)
    except Exception as e:
        print(f"[-] crt.sh failed: {e}")
        return []

def amass_enum(domain):
    print("[*] Running amass...")
    try:
        result = subprocess.run(['amass', 'enum', '-d', domain, '-silent'],
                                capture_output=True, text=True)
        return result.stdout.strip().splitlines()
    except Exception as e:
        print(f"[-] Amass failed: {e}")
        return []

def assetfinder_enum(domain):
    print("[*] Running assetfinder...")
    try:
        result = subprocess.run(['assetfinder', '--subs-only', domain],
                                capture_output=True, text=True)
        return result.stdout.strip().splitlines()
    except Exception as e:
        print(f"[-] Assetfinder failed: {e}")
        return []

def run_subdomain_enum(domain, tools):
    all_subs = []

    if 'subfinder' in tools:
        all_subs += subfinder_enum(domain)
    if 'crtsh' in tools:
        all_subs += crtsh_enum(domain)
    if 'amass' in tools:
        all_subs += amass_enum(domain)
    if 'assetfinder' in tools:
        all_subs += assetfinder_enum(domain)

    return sorted(set(all_subs))

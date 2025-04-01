import subprocess
import requests

# Already existing functions: subfinder_enum, crtsh_enum

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

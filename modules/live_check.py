import subprocess
import requests

def live_check_httpx(domains):
    print("[*] Running httpx...")
    try:
        result = subprocess.run(['httpx', '-silent'],
                                input="\n".join(domains),
                                capture_output=True, text=True)
        return result.stdout.strip().splitlines()
    except Exception as e:
        print(f"[-] httpx failed: {e}")
        return []

def live_check_httprobe(domains):
    print("[*] Running httprobe...")
    try:
        result = subprocess.run(['httprobe'],
                                input="\n".join(domains),
                                capture_output=True, text=True)
        return result.stdout.strip().splitlines()
    except Exception as e:
        print(f"[-] httprobe failed: {e}")
        return []

def live_check_custom(domains):
    print("[*] Running custom Python-based check...")
    live = []
    for domain in domains:
        url = f"http://{domain}"
        try:
            r = requests.get(url, timeout=5)
            if r.status_code < 400:
                live.append(url)
        except:
            pass
        try:
            r = requests.get(f"https://{domain}", timeout=5)
            if r.status_code < 400:
                live.append(f"https://{domain}")
        except:
            pass
    return live

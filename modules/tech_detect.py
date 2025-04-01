import subprocess
import requests

def detect_with_whatweb(urls):
    print("[*] Running whatweb...")
    results = []
    try:
        for url in urls:
            result = subprocess.run(['whatweb', url, '--no-errors'],
                                    capture_output=True, text=True)
            results.append(result.stdout.strip())
    except Exception as e:
        print(f"[-] whatweb failed: {e}")
    return results

def detect_with_custom(urls):
    print("[*] Running custom tech detection (headers)...")
    tech_results = []
    for url in urls:
        try:
            r = requests.get(url, timeout=5)
            headers = r.headers
            server = headers.get("Server", "Unknown")
            powered_by = headers.get("X-Powered-By", "Unknown")
            tech_results.append(f"{url} | Server: {server}, X-Powered-By: {powered_by}")
        except Exception as e:
            tech_results.append(f"{url} | ERROR: {e}")
    return tech_results

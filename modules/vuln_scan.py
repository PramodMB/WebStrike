import subprocess

def run_nuclei(urls):
    print("[*] Running nuclei...")
    results = []
    for url in urls:
        output = f"output/nuclei_{url.replace('http://', '').replace('https://', '').replace('/', '_')}.txt"
        try:
            subprocess.run(['nuclei', '-u', url, '-o', output], check=True)
            results.append(f"{url} | results saved to {output}")
        except subprocess.CalledProcessError:
            results.append(f"{url} | nuclei failed")
    return results

def run_nikto(urls):
    print("[*] Running nikto...")
    results = []
    for url in urls:
        try:
            output = f"output/nikto_{url.replace('http://', '').replace('https://', '').replace('/', '_')}.txt"
            subprocess.run(['nikto', '-h', url, '-o', output, '-Format', 'txt'], check=True)
            results.append(f"{url} | results saved to {output}")
        except subprocess.CalledProcessError:
            results.append(f"{url} | nikto failed")
    return results

def run_wpscan(urls):
    print("[*] Running WPScan...")
    results = []
    for url in urls:
        try:
            output = f"output/wpscan_{url.replace('http://', '').replace('https://', '').replace('/', '_')}.txt"
            subprocess.run(['wpscan', '--url', url, '--enumerate', 'vp', '--output', output], check=True)
            results.append(f"{url} | results saved to {output}")
        except subprocess.CalledProcessError:
            results.append(f"{url} | wpscan failed or not WP")
    return results

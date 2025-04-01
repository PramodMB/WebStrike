import subprocess
import os

def run_arjun(urls):
    print("[*] Running arjun...")
    results = []
    for url in urls:
        outfile = f"output/arjun_{url.replace('http://', '').replace('https://', '').replace('/', '_')}.txt"
        try:
            subprocess.run(
                ['python3', 'arjun/arjun.py', '--url', url, '--get', '--output', outfile],
                check=True
            )
            results.append(f"{url} | params saved to {outfile}")
        except subprocess.CalledProcessError:
            results.append(f"{url} | arjun failed")
    return results

def run_paramspider(urls):
    print("[*] Running ParamSpider...")
    results = []
    for url in urls:
        outdir = f"output/paramspider_{url.replace('http://', '').replace('https://', '').replace('/', '_')}"
        os.makedirs(outdir, exist_ok=True)
        try:
            subprocess.run(
                ['python3', 'ParamSpider/paramspider.py', '-d', url, '-o', outdir],
                check=True
            )
            results.append(f"{url} | output saved to {outdir}")
        except subprocess.CalledProcessError:
            results.append(f"{url} | paramspider failed")
    return results

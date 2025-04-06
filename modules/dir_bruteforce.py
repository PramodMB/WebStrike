import subprocess
import os

def run_ffuf(urls, wordlist):
    print("[*] Running ffuf...")
    found = []
    for url in urls:
        domain_clean = url.replace("http://", "").replace("https://", "").replace("/", "_")
        output_file = f"output/ffuf_{domain_clean}.txt"
        cmd = f"ffuf -u {url}/FUZZ -w {wordlist} -mc 200,204,301,302,403 -of csv -o {output_file} -t 50"
        try:
            subprocess.run(cmd, shell=True, check=True)
            found.append(f"{url} | ffuf completed. Results saved in {output_file}")
        except subprocess.CalledProcessError:
            found.append(f"{url} | ffuf failed")
    return found

def run_dirsearch(urls, wordlist):
    print("[*] Running dirsearch...")
    found = []
    dirsearch_path = os.path.join(os.path.dirname(__file__), "../dirsearch/dirsearch.py")

    for url in urls:
        domain_clean = url.replace("http://", "").replace("https://", "").replace("/", "_")
        output_file = f"output/dirsearch_{domain_clean}.txt"
        cmd = f"python3 {dirsearch_path} -u {url} -e php,html,js -w {wordlist} -t 20 --plain-text-report={output_file}"
        try:
            subprocess.run(cmd, shell=True, check=True)
            found.append(f"{url} | dirsearch completed. Results saved in {output_file}")
        except subprocess.CalledProcessError:
            found.append(f"{url} | dirsearch failed")
    return found


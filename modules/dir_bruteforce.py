import subprocess
import os

def run_ffuf(urls, wordlist):
    print("[*] Running ffuf...")
    found = []
    for url in urls:
        output_file = f"output/ffuf_{url.replace('http://','').replace('https://','').replace('/','_')}.txt"
        cmd = f"ffuf -u {url}/FUZZ -w {wordlist} -mc 200,204,301,302,403 -of csv -o {output_file} -t 50"
        try:
            subprocess.run(cmd, shell=True, check=True)
            found.append(f"Results saved: {output_file}")
        except subprocess.CalledProcessError:
            found.append(f"{url} | ffuf failed")
    return found

def run_dirsearch(urls, wordlist):
    print("[*] Running dirsearch...")
    found = []
    for url in urls:
        cmd = f"python3 dirsearch.py -u {url} -e php,html,js -w {wordlist} -t 20 --plain-text-report=output/dirsearch_{url.replace('http://','').replace('https://','').replace('/','_')}.txt"
        try:
            subprocess.run(cmd, shell=True, check=True)
            found.append(f"{url} | results saved.")
        except subprocess.CalledProcessError:
            found.append(f"{url} | dirsearch failed")
    return found

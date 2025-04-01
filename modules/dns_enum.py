import subprocess

def run_dnsrecon(domain):
    print("[*] Running dnsrecon...")
    outfile = f"output/dnsrecon_{domain}.txt"
    try:
        subprocess.run(['dnsrecon', '-d', domain, '-a', '-j', outfile], check=True)
        return [f"DNSRecon output saved to {outfile}"]
    except subprocess.CalledProcessError:
        return [f"dnsrecon failed for {domain}"]

def run_dnsenum(domain):
    print("[*] Running dnsenum...")
    outfile = f"output/dnsenum_{domain}.txt"
    try:
        subprocess.run(['dnsenum', domain, '--enum', '-o', outfile], check=True)
        return [f"DNSEnum output saved to {outfile}"]
    except subprocess.CalledProcessError:
        return [f"dnsenum failed for {domain}"]

# WebStrike 🛡️
A powerful web application security scanner built by Pramod ⚔️

## 🧰 Features
- Subdomain Enum (subfinder, amass, crt.sh)
- Live Host Check (httpx, httprobe)
- Tech Stack Detection (whatweb)
- Directory Bruteforce (ffuf, dirsearch)
- Parameter Discovery (arjun, paramspider)
- DNS Enum (dnsrecon, dnsenum)
- Vulnerability Scanning (nuclei, nikto, wpscan)
- Exploit PoC (dalfox, sqlmap, redirect check)
- Report Generation (HTML + PDF)

## 🚀 Setup (Kali / Ubuntu)
```bash
git clone https://github.com/yourusername/webstrike.git
cd webstrike
chmod +x setup.sh
./setup.sh

To run the tool - python3 webstrike.py
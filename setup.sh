#!/bin/bash
echo "[*] Installing WebStrike dependencies..."

# Python dependencies
pip3 install -r requirements.txt

# OS tools
apt update
apt install -y amass assetfinder subfinder httpx ffuf dirsearch \
    dnsenum dnsrecon nuclei nikto wpscan sqlmap whatweb golang

# Ensure Go is installed for tools like subfinder & httpx
if ! command -v go &> /dev/null; then
    echo "⚠️ Go is required for some tools like subfinder. Please install manually."
fi

echo "[+] Setup complete."

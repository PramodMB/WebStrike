def save_output(filepath, data):
    try:
        with open(filepath, 'w') as f:
            for item in data:
                f.write(item + '\n')
        print(f"[+] Output saved to {filepath}")
    except Exception as e:
        print(f"[-] Error saving file: {e}")

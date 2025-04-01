from .tools import subfinder_enum, crtsh_enum, amass_enum, assetfinder_enum

def run_subdomain_enum(domain, tools):
    all_subs = set()

    if 'subfinder' in tools:
        all_subs.update(subfinder_enum(domain))

    if 'crtsh' in tools:
        all_subs.update(crtsh_enum(domain))

    if 'amass' in tools:
        all_subs.update(amass_enum(domain))

    if 'assetfinder' in tools:
        all_subs.update(assetfinder_enum(domain))

    return sorted(all_subs)

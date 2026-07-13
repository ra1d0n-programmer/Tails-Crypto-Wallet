# config.py - Proxy configuration

import os

PROXY_FILE = "proxy_config.txt"

def get_proxy_from_user():
    """Ask user for proxy on first run"""
    
    if os.path.exists(PROXY_FILE):
        with open(PROXY_FILE, 'r') as f:
            saved_proxy = f.read().strip()
        print(f"📁 Found saved proxy: {saved_proxy}")
        use_saved = input("Use saved proxy? (y/n): ").strip().lower()
        if use_saved == 'y':
            return saved_proxy
    
    print("\n" + "=" * 60)
    print("  🔧 ENTER YOUR PROXY")
    print("=" * 60)
    print("Examples:")
    print("  - Tor:            socks5h://127.0.0.1:9050")
    print("  - SOCKS5 proxy:   socks5://192.168.1.5:1080")
    print("  - HTTP proxy:     http://proxy.company.com:8080")
    print("  - No proxy:       none")
    print("=" * 60)
    
    proxy = input("\nEnter your proxy: ").strip()
    
    if proxy.lower() == 'none':
        proxy = None
    
    if proxy:
        save = input("Save proxy for future runs? (y/n): ").strip().lower()
        if save == 'y':
            with open(PROXY_FILE, 'w') as f:
                f.write(proxy)
            print("✅ Proxy saved to proxy_config.txt")
    
    return proxy

USER_PROXY = get_proxy_from_user()

if USER_PROXY:
    PROXY_CONFIG = {
        'http': USER_PROXY,
        'https': USER_PROXY
    }
else:
    PROXY_CONFIG = {
        'http': None,
        'https': None
    }

TORRC_PATH = "/etc/tor/torrc"
TIMEOUT = 60
MAX_RETRIES = 3
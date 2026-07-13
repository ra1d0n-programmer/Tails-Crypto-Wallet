# network.py - Network requests through user's proxy

import time
import subprocess
import requests
from config import PROXY_CONFIG, TIMEOUT, MAX_RETRIES

def configure_tor_with_bridges(bridges: list):
    """Configure Tor with bridges"""
    
    torrc_content = """
UseBridges 1
ClientTransportPlugin obfs4 exec /usr/bin/obfs4proxy
ClientTransportPlugin snowflake exec /usr/bin/snowflake-client
"""
    for bridge in bridges:
        torrc_content += f"Bridge {bridge}\n"
    
    try:
        with open("/etc/tor/torrc", 'w') as f:
            f.write(torrc_content)
        subprocess.run(["sudo", "systemctl", "restart", "tor"], check=True)
        print("Tor restarting with new bridges...")
        time.sleep(10)
        return True
    except Exception as e:
        print(f"Tor configuration error: {e}")
        return False

def check_tor_connection():
    """Check if Tor is working"""
    try:
        session = requests.Session()
        session.proxies = PROXY_CONFIG
        response = session.get('https://check.torproject.org/', timeout=10)
        return 'Congratulations' in response.text
    except:
        return False

def wait_for_tor(timeout: int = 60):
    """Wait for Tor to connect"""
    print("Waiting for Tor connection...")
    start = time.time()
    while time.time() - start < timeout:
        if check_tor_connection():
            print("Tor connected successfully!")
            return True
        time.sleep(2)
    print("Failed to connect to Tor")
    return False

def make_request(url: str, params: dict = None) -> dict:
    """Make HTTP request through user's proxy"""
    
    session = requests.Session()
    
    if PROXY_CONFIG['http']:
        session.proxies = PROXY_CONFIG
        print(f"Using proxy: {PROXY_CONFIG['http']}")
    else:
        print("Direct connection (no proxy)")
    
    for attempt in range(MAX_RETRIES):
        try:
            response = session.get(url, params=params, timeout=TIMEOUT)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            print(f"Timeout, attempt {attempt + 1}/{MAX_RETRIES}")
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)
    
    return None
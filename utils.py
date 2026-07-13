# utils.py - Helper functions

import os
from cryptography.fernet import Fernet
import base64

def encrypt_data(data: str, password: str) -> str:
    """Encrypt data with password"""
    key = base64.urlsafe_b64encode(password.ljust(32)[:32].encode())
    cipher = Fernet(key)
    return cipher.encrypt(data.encode()).decode()

def decrypt_data(encrypted: str, password: str) -> str:
    """Decrypt data with password"""
    key = base64.urlsafe_b64encode(password.ljust(32)[:32].encode())
    cipher = Fernet(key)
    return cipher.decrypt(encrypted.encode()).decode()

def save_bridges(bridges: list, filename: str = "bridges.txt"):
    """Save bridges to file"""
    with open(filename, 'w') as f:
        for bridge in bridges:
            f.write(bridge + '\n')

def load_bridges(filename: str = "bridges.txt") -> list:
    """Load bridges from file"""
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def print_header(text: str):
    """Print formatted header"""
    clear_screen()
    print("=" * 60)
    print(f"  {text}")
    print("=" * 60)
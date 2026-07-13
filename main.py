#!/usr/bin/env python3
# main.py - Anonymous Crypto Wallet

import sys
import time
import os
from utils import clear_screen, print_header, save_bridges, load_bridges
from network import configure_tor_with_bridges, wait_for_tor
from wallet import generate_seed_phrase, create_wallet_from_seed, get_balance
from colorama import init, Fore

init(autoreset=True)

def menu_configure_proxy():
    """Reconfigure proxy settings"""
    print_header("🔧 PROXY CONFIGURATION")
    
    if os.path.exists("proxy_config.txt"):
        os.remove("proxy_config.txt")
        print("✅ Saved proxy removed")
    
    print("🔄 Please restart the program to enter new proxy")
    input("\nPress Enter to continue...")

def menu_setup_tor():
    """Configure Tor with bridges"""
    print_header("🔐 TOR BRIDGE CONFIGURATION")
    
    print(Fore.CYAN + """
    ┌─────────────────────────────────────────────────────────────┐
    │  HOW TO GET BRIDGES:                                       │
    │  1. Open Telegram                                          │
    │  2. Search for @GetBridgesBot                             │
    │  3. Click "Start" and select "obfs4" bridges              │
    │  4. Copy the 3 bridge lines                               │
    │  5. Paste them below (one per line)                      │
    └─────────────────────────────────────────────────────────────┘
    """)
    
    saved_bridges = load_bridges()
    if saved_bridges:
        print(f"📁 Found {len(saved_bridges)} saved bridges")
        use_saved = input("Use saved bridges? (y/n): ").strip().lower()
        if use_saved == 'y':
            bridges = saved_bridges
        else:
            bridges = []
    else:
        bridges = []
    
    if not bridges:
        print("\n📝 Paste your bridges from @GetBridgesBot:")
        print("   (Enter one line at a time, empty line to finish)\n")
        while True:
            line = input("> ").strip()
            if not line:
                break
            bridges.append(line)
    
    if not bridges:
        print("❌ No bridges provided!")
        return False
    
    save = input("\n💾 Save bridges for future use? (y/n): ").strip().lower()
    if save == 'y':
        save_bridges(bridges)
        print("✅ Bridges saved to bridges.txt")
    
    print("\n🔄 Configuring Tor with bridges...")
    if configure_tor_with_bridges(bridges):
        if wait_for_tor(timeout=30):
            return True
    
    return False

def menu_create_wallet():
    """Create a new wallet"""
    print_header("🆕 CREATE NEW WALLET")
    
    print("Generating secure seed phrase (24 words)...")
    seed = generate_seed_phrase()
    wallet = create_wallet_from_seed(seed)
    
    print(Fore.YELLOW + "\n" + "=" * 60)
    print(Fore.GREEN + "  ⚠️  SAVE THESE WORDS IN A SECURE PLACE!")
    print(Fore.YELLOW + "=" * 60)
    print(Fore.CYAN + f"\nSEED PHRASE:\n{seed}")
    print(Fore.YELLOW + "\n" + "=" * 60)
    print(Fore.RED + "  🔴 NEVER share this phrase with anyone!")
    print(Fore.RED + "  🔴 Anyone with these words can steal your funds!")
    print(Fore.YELLOW + "=" * 60)
    
    print(f"\n📫 Address: {wallet['address']}")
    print(f"🔑 Private Key (WIF): {wallet['private_key']}")
    
    input("\nPress Enter to continue...")

def menu_check_balance():
    """Check wallet balance"""
    print_header("💰 CHECK BALANCE")
    
    address = input("Enter Bitcoin address: ").strip()
    if not address:
        print("❌ Address cannot be empty")
        return
    
    print(f"\n🔍 Checking balance for {address}...")
    balance = get_balance(address)
    print(f"\n✅ Balance: {balance} BTC")
    input("\nPress Enter to continue...")

def menu_main():
    """Main menu"""
    while True:
        clear_screen()
        print(Fore.CYAN + """
    ╔═══════════════════════════════════════════════╗
    ║     🛡️  ANONYMOUS CRYPTO WALLET             ║
    ║     Secure · Private · Tails Ready          ║
    ╚═══════════════════════════════════════════════╝
        """)
        print(Fore.WHITE + """
    [1] 🔧  Configure Proxy
    [2] 🔐  Configure Tor with Bridges
    [3] 🆕  Create New Wallet
    [4] 💰  Check Balance
    [5] 🚪  Exit
        """)
        
        choice = input("Select option: ").strip()
        
        if choice == '1':
            menu_configure_proxy()
        elif choice == '2':
            menu_setup_tor()
        elif choice == '3':
            menu_create_wallet()
        elif choice == '4':
            menu_check_balance()
        elif choice == '5':
            print("\n👋 Stay private. Stay safe.\n")
            sys.exit(0)
        else:
            print("❌ Invalid option")
            time.sleep(1)

if __name__ == "__main__":
    try:
        menu_main()
    except KeyboardInterrupt:
        print("\n\n👋 Exiting...")
        sys.exit(0)
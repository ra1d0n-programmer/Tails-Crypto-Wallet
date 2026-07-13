# Anonymous Crypto Wallet

A privacy-first cryptocurrency wallet designed for Tails OS with Tor bridge support.

**No KYC. No registration. No traces.**

---

## Features

- Custom Proxy Support — Enter your own proxy (Tor, SOCKS5, HTTP)
- Tor Bridges Integration — Connect via @GetBridgesBot
- BIP-39 / BIP-32 — 24-word seed phrase with HD wallet support
- Fully Anonymous — All requests routed through your proxy
- Tails Ready — Runs in RAM, leaves no traces
- Open Source — MIT License

---

## Prerequisites

- Tails OS 5.0+ (or any Linux with Tor)
- Python 3.8+
- Internet connection
- Telegram (to get bridges from @GetBridgesBot)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ra1d0n-programmer/tails-wallet.git
cd tails-wallet```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the wallet

```bash
python3 main.py
```

---

First Run: Proxy Configuration

On first launch, you will be prompted to enter your proxy:

```
================================================================
  ENTER YOUR PROXY
================================================================
Examples:
  - Tor:            socks5h://127.0.0.1:9050
  - SOCKS5 proxy:   socks5://192.168.1.5:1080
  - HTTP proxy:     http://proxy.company.com:8080
  - No proxy:       none
================================================================

Enter your proxy: socks5h://127.0.0.1:9050
Save proxy for future runs? (y/n): y
Proxy saved to proxy_config.txt
```

---

Getting Tor Bridges (Optional)

If you want to use Tor with bridges:

1. Open Telegram
2. Search for @GetBridgesBot
3. Click "Start" and select "obfs4" bridges
4. Copy the 3 bridge lines
5. Paste them into the wallet (Option 2 in main menu)

---

Usage

Main Menu

```
============================================================
    ANONYMOUS CRYPTO WALLET
    Secure · Private · Tails Ready
============================================================

[1] Configure Proxy
[2] Configure Tor with Bridges
[3] Create New Wallet
[4] Check Balance
[5] Exit
```

1. Configure Proxy

· Change or remove your proxy settings
· Settings are saved for future runs

2. Configure Tor with Bridges

· Enter bridges from @GetBridgesBot
· Wallet restarts Tor with these bridges

3. Create Wallet

· Generates 24-word seed phrase
· Displays Bitcoin address & private key
· SAVE THE SEED PHRASE OFFLINE!

4. Check Balance

· Enter any Bitcoin address
· Wallet fetches balance via your proxy

---

Security Notes

· ISP tracking: Use Tor proxy with bridges
· Persistence: Run on Tails (RAM only)
· Key compromise: Never share your seed phrase
· Phishing: Open source code — verify yourself

---

Dependencies

· requests==2.31.0 — HTTP requests through proxy
· mnemonic==0.20 — BIP-39 seed generation
· bip32utils==0.3.2 — BIP-32 HD wallet
· cryptography==41.0.7 — Encryption utilities
· pysocks==1.7.1 — SOCKS5 proxy support
· colorama==0.4.6 — Terminal colors

---

Development Roadmap

· Custom proxy support
· Tor bridge configuration
· Wallet creation (BIP-39/32)
· Balance checking
· Send transactions
· Multi-coin support (ETH, XMR)
· QR code scanning

---

Contributing

Pull requests are welcome!

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

Disclaimer

USE AT YOUR OWN RISK.

· This software is for educational purposes
· You are responsible for your private keys
· The developers are not liable for any financial loss
· Always test with small amounts first

---

License

MIT License — see LICENSE file for details.

---

Why This Project?

Privacy is not a crime.

This wallet was built for:

· Journalists protecting sources
· Activists in censored regions
· Anyone who values financial privacy

---

Stay private. Stay safe.

# wallet.py - Wallet generation (BIP-39 / BIP-32)

from mnemonic import Mnemonic
from bip32utils import BIP32Key

def generate_seed_phrase(strength: int = 256) -> str:
    """Generate 24-word seed phrase"""
    mnemo = Mnemonic("english")
    return mnemo.generate(strength=strength)

def create_wallet_from_seed(seed_phrase: str, passphrase: str = ""):
    """Create wallet from seed phrase (BIP-32 path: m/44'/0'/0'/0/0)"""
    
    mnemo = Mnemonic("english")
    
    if not mnemo.check(seed_phrase):
        raise ValueError("Invalid seed phrase")
    
    seed = mnemo.to_seed(seed_phrase, passphrase=passphrase)
    
    root_key = BIP32Key.fromEntropy(seed)
    
    key = root_key
    key = key.ChildKey(44 | 0x80000000)
    key = key.ChildKey(0 | 0x80000000)
    key = key.ChildKey(0 | 0x80000000)
    key = key.ChildKey(0)
    address_key = key.ChildKey(0)
    
    return {
        'address': address_key.Address(),
        'private_key': address_key.WalletImportFormat(),
        'seed_phrase': seed_phrase,
        'public_key': address_key.PublicKey().toHex()
    }

def get_balance(address: str, coin: str = "bitcoin") -> float:
    """Get balance from blockchain API"""
    from network import make_request
    
    if coin == "bitcoin":
        url = f"https://blockstream.info/api/address/{address}"
        data = make_request(url)
        if data and 'chain_stats' in data:
            return data['chain_stats']['balance'] / 1e8
    
    return 0.0
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
import os
import base64

# --- Symmetric Key Generation (AES) ---
def generate_aes_key():
    # Generate a random 256-bit key (32 bytes)
    key = os.urandom(32)
    print("AES Key (Base64):", base64.b64encode(key).decode())
    return key

# --- Asymmetric Key Generation (RSA) ---
def generate_rsa_keypair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,  # 2048-bit RSA key
        backend=default_backend()
    )
    public_key = private_key.public_key()
    print("RSA Private Key:", private_key)
    print("RSA Public Key:", public_key)
    return private_key, public_key

# --- Demo ---
if __name__ == "__main__":
    print("🔑 Symmetric Key Generation (AES):")
    aes_key = generate_aes_key()
    
    print("\n🔑 Asymmetric Key Generation (RSA):")
    private_key, public_key = generate_rsa_keypair()

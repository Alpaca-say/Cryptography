import os
import base64
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Generate a 32-byte key for AES-256
key = os.urandom(32)

def encrypt(plaintext, key):
    # Generate random IV
    iv = os.urandom(16)

    # Pad plaintext
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    # Create AES cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()

    # Encrypt data
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Combine IV and ciphertext
    encrypted = iv + ciphertext

    return base64.b64encode(encrypted).decode()

def decrypt(encrypted_text, key):
    encrypted_data = base64.b64decode(encrypted_text)

    # Extract IV and ciphertext
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]

    # Create AES cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()

    # Decrypt data
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove padding
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext.decode()

# Main Program
message = input("Enter message to encrypt: ")

encrypted = encrypt(message, key)
print("\nEncrypted Text:")
print(encrypted)

decrypted = decrypt(encrypted, key)
print("\nDecrypted Text:")
print(decrypted)
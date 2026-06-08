
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Step 1: Generate RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

print("RSA Key Pair Generated Successfully!")

# Step 2: Message to encrypt
message = "Hello, Asymmetric Cryptography!"
print("\nOriginal Message:")
print(message)

# Step 3: Encrypt using the PUBLIC key
encrypted_message = public_key.encrypt(
    message.encode(),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\nEncrypted Message:")
print(encrypted_message)

# Step 4: Decrypt using the PRIVATE key
decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\nDecrypted Message:")
print(decrypted_message.decode())
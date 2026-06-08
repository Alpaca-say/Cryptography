from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Generate RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

# Test message
message = b"RSA Validation Test"

print("Original Message:")
print(message.decode())

# Encrypt
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\nEncryption Successful")
print("Ciphertext Length:", len(ciphertext), "bytes")

# Decrypt
decrypted_message = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\nDecryption Successful")
print("Recovered Message:")
print(decrypted_message.decode())

# Validation
if message == decrypted_message:
    print("\nTEST PASSED")
    print("Original and decrypted messages match.")
else:
    print("\nTEST FAILED")
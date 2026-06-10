def rc4(key, plaintext):
    # Key Scheduling Algorithm (KSA)
    S = list(range(256))
    j = 0

    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-Random Generation Algorithm (PRGA)
    i = 0
    j = 0
    keystream = []

    for _ in range(len(plaintext)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]

        t = (S[i] + S[j]) % 256
        keystream.append(S[t])

    # Encryption/Decryption
    result = []
    for p, k in zip(plaintext.encode(), keystream):
        result.append(p ^ k)

    return bytes(result)


print("=" * 50)
print("RC4 STREAM CIPHER SIMULATION")
print("=" * 50)

key = input("Enter Secret Key: ")
message = input("Enter Message: ")

# Encrypt
ciphertext = rc4(key, message)

print("\n--- Encryption ---")
print("Plaintext :", message)
print("Ciphertext (Hex):", ciphertext.hex())

# Decrypt
decrypted = rc4(key, ciphertext.decode('latin1'))

print("\n--- Decryption ---")
print("Recovered Text:", decrypted.decode())
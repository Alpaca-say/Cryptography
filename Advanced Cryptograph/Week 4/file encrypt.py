from cryptography.fernet import Fernet

# Generate and save a key
key = Fernet.generate_key()

with open("secret.key", "wb") as key_file:
    key_file.write(key)

# Load the key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Encrypt a file
with open("C:\Users\Alpaca\Desktop\text.txt", "rb") as file:
    original_data = file.read()

encrypted_data = cipher.encrypt(original_data)

with open("sample_encrypted.txt", "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)

print("File encrypted successfully!")

# Decrypt the file
with open("sample_encrypted.txt", "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

decrypted_data = cipher.decrypt(encrypted_data)

with open("sample_decrypted.txt", "wb") as decrypted_file:
    decrypted_file.write(decrypted_data)

print("File decrypted successfully!")
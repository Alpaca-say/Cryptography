from cryptography.fernet import Fernet

# Generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as secret.key")

# Load the key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt a file
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        original_data = file.read()

    encrypted_data = fernet.encrypt(original_data)

    with open(filename + ".encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"File encrypted successfully: {filename}.encrypted")

# Decrypt a file
def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    output_file = filename.replace(".encrypted", ".decrypted")

    with open(output_file, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"File decrypted successfully: {output_file}")

# Main Menu
while True:
    print("\n===== SECURE FILE LOCKER =====")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        generate_key()

    elif choice == "2":
        filename = input("Enter file name to encrypt: ")
        encrypt_file(filename)

    elif choice == "3":
        filename = input("Enter encrypted file name: ")
        decrypt_file(filename)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
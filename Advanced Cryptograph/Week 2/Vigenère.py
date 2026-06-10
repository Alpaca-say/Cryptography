def validate_key(key):
    return key.isalpha()

while True:
    print("\n=== Vigenère Cipher Program ===")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "3":
        print("Exiting program...")
        break

    if choice not in ["1", "2"]:
        print("Error: Please enter 1, 2, or 3.")
        continue

    message = input("Enter the message: ")

    if not message.strip():
        print("Error: Message cannot be empty.")
        continue

    key = input("Enter the key (letters only): ")

    if not validate_key(key):
        print("Error: Key must contain letters only.")
        continue

    print("Input validation successful!")

    # Placeholder for encryption/decryption
    if choice == "1":
        print("Proceeding with encryption...")
    else:
        print("Proceeding with decryption...")
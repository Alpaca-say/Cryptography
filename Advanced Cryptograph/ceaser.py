def caesar_cipher(text, shift, mode):
    result = ""

    if mode.lower() == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            # Determine ASCII offset
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            # Shift character
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            # Keep spaces, numbers, and symbols unchanged
            result += char

    return result


# Main Program
print("=== Caesar Cipher Program ===")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
mode = input("Encrypt or Decrypt? ")

output = caesar_cipher(message, shift, mode)

print(f"\nResult: {output}")

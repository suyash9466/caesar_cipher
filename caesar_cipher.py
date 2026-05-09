def caesar_encrypt(text, shift):
    result = []
    shift = shift % 26

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shifted = (ord(ch) - base + shift) % 26
            result.append(chr(base + shifted))
        else:
            result.append(ch)

    return ''.join(result)

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def brute_force(ciphertext):
    print("\n[*] Brute force — all 25 possible shifts:\n")
    for shift in range(1, 26):
        attempt = caesar_decrypt(ciphertext, shift)
        print(f"  Shift {shift:2d}: {attempt}")

def get_shift():
    while True:
        try:
            val = int(input("Enter shift value (1-25): "))
            if 1 <= val <= 25:
                return val
            print("  Shift must be between 1 and 25.")
        except ValueError:
            print("  Please enter a valid integer.")

def main():
    print("=" * 50)
    print("       Caesar Cipher")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("  1. Encrypt a message")
        print("  2. Decrypt a message")
        print("  3. Brute force decrypt")
        print("  4. Exit")

        choice = input("\nChoose (1-4): ").strip()

        if choice == '1':
            msg = input("Enter message to encrypt: ")
            shift = get_shift()
            encrypted = caesar_encrypt(msg, shift)
            print(f"\n  Original  : {msg}")
            print(f"  Encrypted : {encrypted}")
            print(f"  Shift used: {shift}")

        elif choice == '2':
            msg = input("Enter message to decrypt: ")
            shift = get_shift()
            decrypted = caesar_decrypt(msg, shift)
            print(f"\n  Encrypted : {msg}")
            print(f"  Decrypted : {decrypted}")
            print(f"  Shift used: {shift}")

        elif choice == '3':
            msg = input("Enter ciphertext to brute-force: ")
            brute_force(msg)

        elif choice == '4':
            print("\nBye!\n")
            break

        else:
            print("  Invalid option, try again.")

if __name__ == "__main__":
    main()

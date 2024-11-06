def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    
    # Loop through each character in the text
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine if the letter is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            
            # Encrypt or decrypt the letter depending on the mode
            if mode == 'encrypt':
                shifted = (ord(char) - start + shift) % 26
            elif mode == 'decrypt':
                shifted = (ord(char) - start - shift) % 26
            
            # Convert the shifted character back to a letter
            result += chr(start + shifted)
        else:
            # Non-alphabetical characters are added without change
            result += char
    
    return result


def main():
    print("Welcome to the Caesar Cipher Encryption/Decryption Program!")
    
    # Take input from the user
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (1-25): "))
    
    # Ensure valid shift value
    if shift < 1 or shift > 25:
        print("Invalid shift value. Please enter a number between 1 and 25.")
        return
    
    # Encrypt the message
    encrypted_message = caesar_cipher(message, shift, mode='encrypt')
    print(f"Encrypted Message: {encrypted_message}")
    
    # Decrypt the message
    decrypted_message = caesar_cipher(encrypted_message, shift, mode='decrypt')
    print(f"Decrypted Message: {decrypted_message}")


if __name__ == "__main__":
    main()
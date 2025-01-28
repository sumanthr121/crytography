# vigenere_cipher.py

#  This Function  is to encrypt a message using the Vigenère Cipher
def vigenere_encrypt(plaintext, keyword):
    """
    Encrypts the input 'plaintext' using the Vigenère Cipher method with the given 'keyword'.
    The Vigenère Cipher uses a series of Caesar Ciphers based on the letters of the keyword.
    """
    ciphertext = ""  # This will hold the final encrypted message
    keyword = keyword.upper()  # Convert the keyword to uppercase for uniformity
    i = 0  # This index will track the position of the keyword characters

    # Loop through each character in the plaintext
    for char in plaintext.upper():  # Convert the plaintext to uppercase to avoid case differences
        if char.isalpha(): 
            # The shift is determined by the position of the current keyword letter
            shift = ord(keyword[i % len(keyword)]) - 65  # 'A' = 65, so this maps letters to a shift value
            # Encrypt the character by shifting it based on the current keyword letter
            ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
            i += 1  
        else:
            
            ciphertext += char

    return ciphertext  # Return the final encrypted message


# Function to decrypt a message using the Vigenère Cipher
def vigenere_decrypt(ciphertext, keyword):
    """
    Decrypts the input 'ciphertext' using the Vigenère Cipher method with the given 'keyword'.
    This reverses the encryption process to recover the original message.
    """
    plaintext = ""  # This will hold the decrypted message
    keyword = keyword.upper()  # Convert the keyword to uppercase for uniformity
    i = 0  # This index will track the position of the keyword characters

    # Loop through each character in the ciphertext
    for char in ciphertext.upper():  # Convert the ciphertext to uppercase for consistency
        if char.isalpha():  # Only decrypt alphabetic characters
            # The shift is determined by the position of the current keyword letter
            shift = ord(keyword[i % len(keyword)]) - 65  # 'A' = 65, so this maps letters to a shift value
            # Decrypt the character by reversing the shift applied during encryption
            plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
            i += 1  # Move to the next character in the keyword
        else:
            # If the character is not a letter (e.g., space, punctuation), keep it as is
            plaintext += char

    return plaintext  # Return the final decrypted message


# Main function where user inputs are taken and the encryption/decryption happens
if __name__ == "__main__":
    # Ask the user to input the message to encrypt
    plaintext = input("Enter the text to encrypt: ").upper()  # Convert input to uppercase
    keyword = input("Enter the keyword for encryption: ").upper()  # Convert keyword to uppercase

    # Encrypt the plaintext using the Vigenère cipher
    encrypted = vigenere_encrypt(plaintext, keyword)
    
    # Decrypt the ciphertext back to the original plaintext
    decrypted = vigenere_decrypt(encrypted, keyword)

    # Output the results
    print(f"Encrypted Text: {encrypted}")  # Show the encrypted version of the message
    print(f"Decrypted Text: {decrypted}")  # Show the original message after decryption

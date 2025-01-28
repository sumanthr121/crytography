# rsa.py
from extended_euclid import mod_inverse

# Function to encrypt the message using RSA encryption
def encrypt(message, e, n):
    """
    Encrypts the input message using RSA encryption.
    
    Parameters:
    - message: The plaintext message to be encrypted (as a string).
    - e: The public key exponent.
    - n: The modulus n (n = p * q, where p and q are prime numbers).
    
    Returns:
    - A list of encrypted numeric values (ciphertext).
    """
    # Convert each character of the message to its ASCII value, raise it to the power of e, and take modulo n
    return [pow(ord(char), e, n) for char in message]

# Function to decrypt the ciphertext using RSA decryption
def decrypt(ciphertext, d, n):
    """
    Decrypts the input ciphertext using RSA decryption.
    
    Parameters:
    - ciphertext: The encrypted message (as a list of numeric values).
    - d: The private key exponent.
    - n: The modulus n (n = p * q).
    
    Returns:
    - The decrypted message (as a string).
    """
    # For each encrypted number, raise it to the power of d and take modulo n to get back the original character
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Main block where user inputs are taken and encryption/decryption is performed
if __name__ == "__main__":
    # Get two prime numbers, p and q, from the user
    p = int(input("Enter the first prime number (p): "))
    q = int(input("Enter the second prime number (q): "))
    
    # Calculate n, the modulus used in both public and private keys
    n = p * q
    
    # Calculate φ(n) = (p-1) * (q-1), used in calculating the private key
    phi_n = (p - 1) * (q - 1)
    
    # Get the public key exponent e (should be coprime with φ(n))
    e = int(input(f"Enter the value for 'e' (public key exponent): "))
    
    # Compute the private key exponent d using the modular inverse of e modulo φ(n)
    d = mod_inverse(e, phi_n)
    
    if d is None:
        # If d does not exist, print an error message
        print(f"Invalid 'e' value. No modular inverse exists.")
    else:
        # If the modular inverse exists, proceed with encryption and decryption
        message = input("Enter the message to encrypt: ")
        
        # Encrypt the message
        encrypted = encrypt(message, e, n)
        
        # Decrypt the ciphertext back to the original message
        decrypted = decrypt(encrypted, d, n)

        # Output the results: encrypted message and the decrypted message
        print(f"Encrypted Text: {encrypted}")
        print(f"Decrypted Text: {decrypted}")

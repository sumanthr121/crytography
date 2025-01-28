# elgamal.py

# Function to perform ElGamal encryption
def elgamal_encrypt(m, e1, p, g, r):
    """
    Encrypts the message 'm' using the ElGamal encryption algorithm.
    
    Parameters:
    - m: The message (as a numeric value) to be encrypted.
    - e1: The public key part (g^d mod p).
    - p: A large prime number used in the encryption process.
    - g: The generator used in the ElGamal algorithm.
    - r: A random number used to create the ciphertext.
    
    Returns:
    - c1, c2: The two components of the ciphertext.
    """
    # Compute c1 = g^r mod p (first part of the ciphertext)
    c1 = pow(g, r, p)
    
    # Compute c2 = (m * e1^r) mod p (second part of the ciphertext)
    c2 = (m * pow(e1, r, p)) % p
    
    return c1, c2  # Return the ciphertext (c1, c2)

# Function to perform ElGamal decryption
def elgamal_decrypt(c1, c2, p, d):
    """
    Decrypts the ciphertext (c1, c2) using the ElGamal decryption algorithm.
    
    Parameters:
    - c1: The first part of the ciphertext.
    - c2: The second part of the ciphertext.
    - p: A large prime number used in the decryption process.
    - d: The private key used for decryption.
    
    Returns:
    - m: The decrypted message (numeric value).
    """
    # Compute the decrypted message m = c2 * (c1^(-d)) mod p
    m = (c2 * pow(c1, p - 1 - d, p)) % p
    
    return m  # Return the decrypted message

# Main block where we take user inputs and perform encryption and decryption
if __name__ == "__main__":
    # Get user input for the prime number p and generator g
    p = int(input("Enter the prime number p: "))
    g = int(input("Enter the generator g: "))
    
    # Get the private key d
    d = int(input("Enter the private key d: "))
    
    # Compute e1 = g^d mod p (public key part)
    e1 = pow(g, d, p)
    
    # Get the random number r (used in the encryption process)
    r = int(input("Enter a random number r: "))
    
    # Get the message to encrypt (as a numeric value)
    m = int(input("Enter the message (numeric value): "))
    
    # Perform encryption
    c1, c2 = elgamal_encrypt(m, e1, p, g, r)
    
    # Perform decryption
    decrypted = elgamal_decrypt(c1, c2, p, d)
    
    # Output the results
    print(f"Encrypted (c1, c2): ({c1}, {c2})")
    print(f"Decrypted Message: {decrypted}")

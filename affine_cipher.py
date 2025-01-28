def affine_encrypt(plain_text,a,b):   
    """
    It basically encrypts the plain text using aphine cypher formula
    """
    cipher_text = "" 
    for char in plain_text:
        if char.isalpha():  # This function basically  process only  alphabetic characters
            x = ord(char.upper()) - 65  # basically. converts  the letters to the numbers as mentioned  (A = 0, B = 1, ..., Z = 25)
            encrypted_char = (a * x + b) % 26 + 65  # Apply Affine Cipher formula
            cipher_text += chr(encrypted_char)
        else:
            cipher_text += char  # If there is a non -Alphabet keept it unchanged . 
    return cipher_text


def affine_decrypt(cipher_text, a, b):
    """
    Decrypts the cipher_text using the Affine Cipher formula. 
    """
    a_inv = mod_inverse(a, 26)  # Get modular inverse of a
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():  # Only process alphabetic characters
            x = ord(char.upper()) - 65  # Convert letter to number
            decrypted_char = (a_inv * (x - b)) % 26 + 65  # Apply Affine Cipher decryption formula
            plain_text += chr(decrypted_char) #  the  plain  txt  is  now beng decrypted here using the formula
        else:
            plain_text += char  # If non-alphabet, keep it unchanged
    return plain_text


def mod_inverse(a, m): # appling the modulus function into 
    """
    Returns the modular inverse of a with respect to m using the Extended Euclidean Algorithm.
    """
    g, x, y = extended_euclid(a, m)
    if g != 1:
        raise Exception(f"Modular inverse of {a} does not exist.") # if there the modulus inverese do not exist do not shows the it raises execption and further gcd is not calculated 
    return x % m


def extended_euclid(a, b):
    """
    Extended Euclidean Algorithm to find gcd of two numbers and the coefficients x and y.
    """
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_euclid(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


# Main code to take the input from the user 
def main():
    print("Affine Cipher")
    
    # Taking plaintext, a, and b  values of a and b as input from the user
    plain_text = input("Enter the plaintext: ")
    a = int(input("Enter the value of a (a must be coprime with 26): ")) #the value of a which you enter must satisfy the condition of coprime of 26
    b = int(input("Enter the value of b: "))
    
    # Checking if 'a' is coprime with 26
    if extended_euclid(a, 26)[0] != 1: # if it is not a coprime as validated it shows error 
        print(f"Error: {a} is not coprime with 26. Please choose another 'a'.")
        return
    
    # Encrypting the plaintext
    encrypted_text = affine_encrypt(plain_text, a, b)
    print("Encrypted text:", encrypted_text)
    
    # Decrypting the ciphertext
    decrypted_text = affine_decrypt(encrypted_text, a, b)
    print("Decrypted text:", decrypted_text)


#  main function
if __name__ == "__main__":
    main()
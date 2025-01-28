# extended_euclid.py

# Function to implement the Extended Euclidean Algorithm
def extended_gcd(a, b):
    """
    This function finds the greatest common divisor (GCD) of two numbers 'a' and 'b'.
    It also returns the coefficients x and y such that: 
    a * x + b * y = gcd(a, b)(formula)
    """
    # Base case: when a becomes 0, the GCD is b, and coefficients are 0 and 1
    if a == 0:
        return b, 0, 1
    
    # Recursive step: apply the Euclidean algorithm
    gcd, x1, y1 = extended_gcd(b % a, a)  # Recursively call with new arguments
    
    # Update x and y based on the recursive results
    x = y1 - (b // a) * x1  # x is updated using the recursive result
    y = x1  # y is updated using the previous x
    return gcd, x, y

# Function to compute the modular inverse of a number 'a' modulo 'm'
def mod_inverse(a, m):
    """
    This function returns the modular inverse of 'a' with respect to modulus 'm'.
    It uses the Extended Euclidean Algorithm to find the inverse such that:
    a * x ≡ 1 (mod m)
    If the inverse does not exist, it returns None.
    """
    gcd, x, y = extended_gcd(a, m)  # Find the GCD and coefficients x, y
    if gcd != 1:
        # If GCD is not 1, the inverse does not exist
        return None
    return x % m  # The modular inverse is the positive remainder when x is divided by m

# Main block to take user inputs and display results
if __name__ == "__main__":
    # Ask the user for the values of 'a' and 'm'
    a = int(input("Enter the value for 'a': "))
    m = int(input("Enter the value for 'm': "))
    
    # Calculate the modular inverse using the mod_inverse function
    inverse = mod_inverse(a, m)
    
    if inverse is None:
        # If no modular inverse exists, inform the user
        print(f"Modular inverse does not exist for a = {a} and m = {m}")
    else:
        # Otherwise, show the modular inverse
        print(f"Modular inverse of {a} mod {m} is {inverse}")

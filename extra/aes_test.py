# editor working


# Import the necessary modules
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Define the encryption and decryption functions
def encrypt(key, plaintext):
    # Generate a random 16-byte initialization vector
    iv = get_random_bytes(16)
    # Create an AES cipher object with the given key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Pad the plaintext to a multiple of 16 bytes
    plaintext_padded = plaintext + b"\0" * (16 - len(plaintext) % 16)
    # Encrypt the padded plaintext
    ciphertext = cipher.encrypt(plaintext_padded)
    # Return the IV and ciphertext as bytes objects
    return iv + ciphertext

def decrypt(key, ciphertext):
    # Extract the IV from the ciphertext
    iv = ciphertext[:16]
    # Create an AES cipher object with the given key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Decrypt the ciphertext
    plaintext_padded = cipher.decrypt(ciphertext[16:])
    # Remove the padding from the plaintext
    plaintext = plaintext_padded.rstrip(b"\0")
    # Return the plaintext as a bytes object
    return plaintext

# Define the key and plaintext
key = b"ThisIsASecretKey"
plaintext = b"Hello, World!"

print(f"key: {key}")
print(f"plaintext: {plaintext}")

# Encrypt the plaintext
ciphertext = encrypt(key, plaintext)
print("Ciphertext:", ciphertext.hex())

# Decrypt the ciphertext
decrypted_plaintext = decrypt(key, ciphertext)
print("Decrypted plaintext:", decrypted_plaintext.decode())

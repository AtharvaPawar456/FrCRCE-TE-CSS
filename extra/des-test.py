# editor working

from cryptography.fernet import Fernet

# Generate a random key
key = Fernet.generate_key()

# Create a Fernet instance with the key
fernet = Fernet(key)
plaintext = "This is a secret message."
# Encode a message using the Fernet instance
message = plaintext.encode()
encrypted = fernet.encrypt(message)

print(f"plaintext: {plaintext}")
print(f"message encoded: {message}")


# Print the encrypted message
print("Encrypted message: ", encrypted)

# Decrypt the message using the same Fernet instance
decrypted = fernet.decrypt(encrypted)

# Print the decrypted message
print("Decrypted message: ", decrypted.decode())

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes


def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext


def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext


# Generate a random 64-bit key
key = get_random_bytes(8)

# Encrypt a plaintext
plaintext = b"Hello DES!"
ciphertext = des_encrypt(key, plaintext)

# Decrypt the ciphertext
decrypted_plaintext = des_decrypt(key, ciphertext)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Plaintext:", decrypted_plaintext)

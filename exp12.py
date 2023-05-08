# import random

# def main():
#     plaintext = "HELLO WORLD"
#     key = generateKey(len(plaintext))
#     print("Plaintext: " + plaintext)
#     ciphertext = encrypt(plaintext, key)
#     print("Ciphertext: " + ciphertext)
#     decryptedText = decrypt(ciphertext, key)
#     print("Decrypted text: " + decryptedText)

# def generateKey(length):
#     key = []
#     for i in range(length):
#         key.append(random.randint(1, 26))
#     return key

# def encrypt(plaintext, key):
#     ciphertext = ""
#     keyIndex = 0
#     for i in range(len(plaintext)):
#         c = plaintext[i]
#         shift = key[keyIndex]
#         encryptedChar = shiftChar(c, shift)
#         ciphertext += encryptedChar
#         keyIndex = (keyIndex + 1) % len(key)
#     return ciphertext

# def decrypt(ciphertext, key):
#     decryptedText = ""
#     keyIndex = 0
#     for i in range(len(ciphertext)):
#         c = ciphertext[i]
#         shift = key[keyIndex]
#         decryptedChar = shiftChar(c, -shift)
#         decryptedText += decryptedChar
#         keyIndex = (keyIndex + 1) % len(key)
#     return decryptedText

# def shiftChar(c, shift):
#     if not c.isalpha():
#         return c
#     asciiOffset = 65 if c.isupper() else 97
#     shifted = ord(c) - asciiOffset + shift
#     shifted %= 26
#     return chr(shifted + asciiOffset)

# if __name__ == "_main_":
#     main()


import numpy as np
key = np.array([[9, 4], [5, 7]])
def string_to_matrix(s):
    return np.array([ord(c) - 97 for c in s])
def matrix_to_string(matrix):
    return ''.join([chr(int(x) + 97) for x in matrix])
def hill_cipher_encrypt(message):
    message_matrix = string_to_matrix(message)
    message_matrix = np.reshape(message_matrix, (-1, 2)).T
    len = message_matrix.shape[1]
    encrypted_matrix = np.mod(np.dot(key, message_matrix), 26)
    encrypted_message = matrix_to_string(encrypted_matrix.T.flatten())
    return encrypted_message

message = "meet me at the usual place at ten rather than eight oclock"
encrypted_message = hill_cipher_encrypt(message)
print("Encrypted message: c",encrypted_message)
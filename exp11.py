# def main():
#     key = [[9, 4], [5, 7]]
#     plaintext = "meet me at the usual place at ten rather than eight oclock"
#     plaintext = ''.join(filter(str.isalpha, plaintext)).upper()
#     n = len(plaintext)
#     if n % 2 != 0:
#         plaintext += "X"
#         n += 1
#     ciphertext = [0] * n
#     for i in range(0, n, 2):
#         c1 = ord(plaintext[i]) - ord('A')
#         c2 = ord(plaintext[i + 1]) - ord('A')
#         ciphertext[i] = (key[0][0] * c1 + key[0][1] * c2) % 26
#         ciphertext[i + 1] = (key[1][0] * c1 + key[1][1] * c2) % 26
#     result = ''
#     for i in range(n):
#         result += chr(ciphertext[i] + ord('A'))
#     print(result)

# if __name__== '_main_':
#     main()


import math
KEY_SIZE = 25
def num_possible_keys():
    total = 1
    for i in range(KEY_SIZE):
        total *= (KEY_SIZE - i)
    return total
keys = num_possible_keys()
print(f"The Playfair cipher has approximately {math.log2(keys):.2f} possible keys.")
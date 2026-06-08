def round_function(block, key):
    return block ^ key

def feistel_encrypt(plaintext, keys):
    left = plaintext[:4]
    right = plaintext[4:]
    for i in range(4):
        new_right = [left[j] ^ round_function(right[j], keys[i]) for j in range(4)]
        left = right
        right = new_right
    return left + right

def feistel_decrypt(ciphertext, keys):
    left = ciphertext[:4]
    right = ciphertext[4:]
    for i in reversed(range(4)):
        new_left = [right[j] ^ round_function(left[j], keys[i]) for j in range(4)]
        right = left
        left = new_left
    return left + right

plaintext = [1, 0, 1, 1, 0, 1, 1, 0]
keys = [3, 7, 5, 2]

ciphertext = feistel_encrypt(plaintext, keys)
decrypted = feistel_decrypt(ciphertext, keys)

print("Original plaintext:", plaintext)
print("Ciphertext:        ", ciphertext)
print("Decrypted:         ", decrypted)
print()
if plaintext == decrypted:
    print("Success! Decryption correctly recovered the original plaintext")
else:
    print("Something went wrong - plaintext does not match")
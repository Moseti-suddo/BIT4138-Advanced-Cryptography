def round_function(block, key):
    return block ^ key

def feistel_encrypt(plaintext, keys):
    left = plaintext[:4]
    right = plaintext[4:]

    print("_" * 45)
    print(f"{'Round':<10} {'Left':<18} {'Right'}")
    print("_" * 45)
    print(f"{'Start':<10} {str(left):<18} {str(right)}")

    for i in range(4):
        new_right = [left[j] ^ round_function(right[j], keys[i]) for j in range(4)]
        left = right
        right = new_right
        print(f"{i+1:<10} {str(left):<18} {str(right)}")

    print("_" * 45)
    return left + right

plaintext = [1, 0, 1, 1, 0, 1, 1, 0]
keys = [3, 7, 5, 2]

print("Plaintext:", plaintext)
print("Keys:", keys)
print()
ciphertext = feistel_encrypt(plaintext, keys)
print()
print("Ciphertext:", ciphertext)
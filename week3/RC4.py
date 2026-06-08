def rc4(key, plaintext):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # the keystream generation and encryption
    i = 0
    j = 0
    ciphertext = []
    for byte in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        ciphertext.append(byte ^ k)

    return ciphertext

key = [75, 69, 89]
plaintext = [72, 69, 76, 76, 79]

print("Key (ascii):", key)
print("Plaintext (ascii):", plaintext)
print("Plaintext (text): HELLO")
print()

ciphertext = rc4(key, plaintext)
print("Ciphertext (bytes):", ciphertext)
print("Ciphertext (hex):", [hex(b) for b in ciphertext])
print()

decrypted = rc4(key, ciphertext)
print("Decrypted (ascii):", decrypted)
print("Decrypted (text): ", ''.join(chr(b) for b in decrypted))
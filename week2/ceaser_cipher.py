def caesar_encrypt(text, shift):
    result = ""
    for letter in text:
        shifted = (ord(letter) - ord('A') + shift) % 26
        result += chr(shifted + ord('A'))
    return result

def caesar_decrypt(text, shift):
    result = ""
    for letter in text:
        shifted = (ord(letter) - ord('A') - shift) % 26
        result += chr(shifted + ord('A'))
    return result

plaintext = "SECURITY"
shift = 4

encrypted = caesar_encrypt(plaintext, shift)
decrypted = caesar_decrypt(encrypted, shift)

print("Plaintext: ", plaintext)
print("Shift:     ", shift)
print("Encrypted: ", encrypted)
print("Decrypted: ", decrypted)
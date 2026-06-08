# Caesar Decrypt
def caesar_decrypt(text, shift):
    result = ""
    for letter in text:
        shifted = (ord(letter) - ord('A') - shift) % 26
        result += chr(shifted + ord('A'))
    return result

# Vigenere Decrypt
def vigenere_decrypt(text, keyword):
    result = ""
    keyword = keyword * (len(text) // len(keyword) + 1)
    keyword = keyword[:len(text)]
    for i in range(len(text)):
        shift = ord(keyword[i]) - ord('A')
        result += chr((ord(text[i]) - ord('A') - shift) % 26 + ord('A'))
    return result

# Caesar
caesar_cipher = "WIGYVMXC"
caesar_plain = caesar_decrypt(caesar_cipher, 4)
print("--- Caesar Cipher ---")
print("Ciphertext: ", caesar_cipher)
print("Decrypted:  ", caesar_plain)

print()

# Vigenere
vigenere_cipher = "XMNZWOR"
vigenere_plain = vigenere_decrypt(vigenere_cipher, "KEY")
print("--- Vigenere Cipher ---")
print("Ciphertext: ", vigenere_cipher)
print("Decrypted:  ", vigenere_plain)
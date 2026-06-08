def vigenere_encrypt(text, keyword):
    result = ""
    keyword = keyword * (len(text) // len(keyword) + 1)
    keyword = keyword[:len(text)]

    print("Letter | Keyword | Shift | Encrypted")
    print("-" * 40)

    for i in range(len(text)):
        shift = ord(keyword[i]) - ord('A')
        encrypted_letter = chr((ord(text[i]) - ord('A') + shift) % 26 + ord('A'))
        print(f"  {text[i]}    |    {keyword[i]}    |   {shift}   |    {encrypted_letter}")
        result += encrypted_letter

    return result

def vigenere_decrypt(text, keyword):
    result = ""
    keyword = keyword * (len(text) // len(keyword) + 1)
    keyword = keyword[:len(text)]

    for i in range(len(text)):
        shift = ord(keyword[i]) - ord('A')
        decrypted_letter = chr((ord(text[i]) - ord('A') - shift) % 26 + ord('A'))
        result += decrypted_letter

    return result

plaintext = "NETWORK"
keyword = "KEY"

print("Plaintext: ", plaintext)
print("Keyword:   ", keyword)
print()
encrypted = vigenere_encrypt(plaintext, keyword)
print()
print("Encrypted: ", encrypted)
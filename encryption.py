from Crypto.Cipher import AES
import os

key = os.urandom(16)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(b'Hello Cryptography!')

print('Key:', key.hex())
print('Ciphertext:', ciphertext.hex())
print('Tag:', tag.hex())
print('AES encryption successful!') 
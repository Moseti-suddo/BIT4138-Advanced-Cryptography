

SBOX = [0x9, 0x4, 0xA, 0xB,
        0xD, 0x1, 0x8, 0x5,
        0x6, 0x2, 0x0, 0x3,
        0xC, 0xE, 0xF, 0x7]

PBOX = [0, 4, 8,  12,
        1, 5, 9,  13,
        2, 6, 10, 14,
        3, 7, 11, 15]

def substitute(block):
    result = 0
    for i in range(4):
        nibble = (block >> (12 - i * 4)) & 0xF
        result |= (SBOX[nibble] << (12 - i * 4))
    return result

def permute(block):
    result = 0
    for i in range(16):
        bit = (block >> (15 - i)) & 1
        result |= (bit << (15 - PBOX[i]))
    return result

def spn_encrypt(block):
    print(f"\n  Input           : {block:016b}  ({block:04X})")

    # Round 1
    after_sub1  = substitute(block)
    after_perm1 = permute(after_sub1)
    print(f"\n  [Round 1]")
    print(f"  After Sub       : {after_sub1:016b}  ({after_sub1:04X})")
    print(f"  After Perm      : {after_perm1:016b}  ({after_perm1:04X})")

    # Round 2
    after_sub2 = substitute(after_perm1)
    print(f"\n  [Round 2]")
    print(f"  After Sub       : {after_sub2:016b}  ({after_sub2:04X})")

    return after_sub2

def text_to_blocks(text):
    if len(text) % 2 != 0:
        text += ' '
    blocks = []
    for i in range(0, len(text), 2):
        block = (ord(text[i]) << 8) | ord(text[i+1])
        blocks.append(block)
    return blocks

def main():
    print("=" * 50)
    print("   SPN - Substitution-Permutation Network")
    print("   BIT4138 Advanced Cryptography")
    print("=" * 50)

    plaintext = input("\nEnter plaintext: ")
    blocks = text_to_blocks(plaintext)

    ciphertext_blocks = []
    for idx, block in enumerate(blocks):
        print(f"\n--- Block {idx + 1}: '{chr(block >> 8)}{chr(block & 0xFF)}' ---")
        cipher_block = spn_encrypt(block)
        ciphertext_blocks.append(cipher_block)

    print(f"\n{'=' * 50}")
    print("RESULTS")
    print(f"{'=' * 50}")
    print(f"Plaintext        : {plaintext}")
    print(f"Ciphertext (hex) : {' '.join(f'{b:04X}' for b in ciphertext_blocks)}")
    print(f"Ciphertext (bin) : {' '.join(f'{b:016b}' for b in ciphertext_blocks)}")
    print("=" * 50)

if __name__ == "__main__":
    main()
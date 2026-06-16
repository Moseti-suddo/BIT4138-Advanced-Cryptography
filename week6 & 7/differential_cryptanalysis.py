
SBOX = [0x9, 0x4, 0xA, 0xB,
        0xD, 0x1, 0x8, 0x5,
        0x6, 0x2, 0x0, 0x3,
        0xC, 0xE, 0xF, 0x7]

def substitute(block):
    result = 0
    for i in range(4):
        nibble = (block >> (12 - i * 4)) & 0xF
        result |= (SBOX[nibble] << (12 - i * 4))
    return result

def xor_difference(a, b):
    return a ^ b

def count_bit_differences(a, b):
    diff = a ^ b
    return bin(diff).count('1')

def main():
    print("=" * 55)
    print("   DIFFERENTIAL CRYPTANALYSIS SIMULATION")
    print("   BIT4138 Advanced Cryptography - Week 7")
    print("=" * 55)

    # User inputs
    p1 = input("\nEnter Plaintext 1: ")
    p2 = input("Enter Plaintext 2: ")

    # Convert to integers
    val1 = int.from_bytes(p1[:2].encode(), 'big')
    val2 = int.from_bytes(p2[:2].encode(), 'big')

    print(f"\n{'─' * 55}")
    print("INPUT ANALYSIS")
    print(f"{'─' * 55}")
    print(f"Plaintext 1      : {p1[:2]}  →  {val1:016b}  ({val1:04X})")
    print(f"Plaintext 2      : {p2[:2]}  →  {val2:016b}  ({val2:04X})")

    # Input difference
    input_diff = xor_difference(val1, val2)
    input_bits  = count_bit_differences(val1, val2)
    print(f"\nInput Difference (XOR) : {input_diff:016b}  ({input_diff:04X})")
    print(f"Bits Different         : {input_bits} / 16")

    # Apply substitution to both
    c1 = substitute(val1)
    c2 = substitute(val2)

    print(f"\n{'─' * 55}")
    print("AFTER SUBSTITUTION")
    print(f"{'─' * 55}")
    print(f"Output 1         : {c1:016b}  ({c1:04X})")
    print(f"Output 2         : {c2:016b}  ({c2:04X})")

    output_diff = xor_difference(c1, c2)
    output_bits = count_bit_differences(c1, c2)
    print(f"\nOutput Difference (XOR): {output_diff:016b}  ({output_diff:04X})")
    print(f"Bits Different         : {output_bits} / 16")

    # Avalanche observation
    print(f"\n{'─' * 55}")
    print("DIFFERENTIAL OBSERVATION")
    print(f"{'─' * 55}")
    print(f"Input bits changed     : {input_bits}")
    print(f"Output bits changed    : {output_bits}")

    if output_bits >= 8:
        print(f"Avalanche Effect       : STRONG ✓")
        print(f"Observation            : Small input change caused significant output change.")
    elif output_bits >= 4:
        print(f"Avalanche Effect       : MODERATE")
        print(f"Observation            : Partial diffusion observed.")
    else:
        print(f"Avalanche Effect       : WEAK ✗")
        print(f"Observation            : Input change had minimal effect on output.")

    print("=" * 55)

if __name__ == "__main__":
    main()
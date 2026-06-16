# comparison.py
print("=" * 55)
print("Feistel Network vs SPN Comparison")
print("=" * 55)

comparison = [
    ("Block operation", "Splits into halves",     "Full block"),
    ("Core components", "Round function",          "S-Box + P-Box"),
    ("Decryption",      "Reverse keys",            "Inverse S-Box"),
    ("Example cipher",  "DES",                     "AES"),
    ("Diffusion",       "Swapping halves",         "Permutation layer"),
]

print(f"\n{'Feature':<20} {'Feistel':<22} {'SPN'}")
print("-" * 55)
for f, feistel, spn in comparison:
    print(f"{f:<20} {feistel:<22} {spn}")
print("=" * 55)
import string

ciphertext = "WIGYVMXCVZNQOPZABIDEFKLMNOPQRSTUVWXYZABCDE"

def frequency_analysis(text):
    print("Letter Frequency Analysis")
    for letter in string.ascii_uppercase:
        count = text.count(letter)
        bar = "#" * count
        print(f"{letter}: {bar} ({count})")

print("Ciphertext:", ciphertext)
print()
frequency_analysis(ciphertext)
print()
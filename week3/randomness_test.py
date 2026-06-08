def frequency_test(bits):
    ones = bits.count(1)
    zeros = bits.count(0)
    return ones, zeros

def runs_test(bits):
    runs = 1
    for i in range(1, len(bits)):
        if bits[i] != bits[i-1]:
            runs += 1
    return runs

def mean_value(bits):
    return sum(bits) / len(bits)

bits = [1,0,1,1,0,1,0,0,1,1,0,1,1,0,1,0,1,0,0,1,
        1,0,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,0,1,1,
        1,0,0,1,0,1,1,0,1,0,1,0,1,1,0,0,1,0,1,1,
        0,1,0,1,0,0,1,1,0,1,1,0,1,0,1,0,0,1,1,0,
        1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,0,1,1,0,1]

ones, zeros = frequency_test(bits)
runs = runs_test(bits)
mean = mean_value(bits)

print("=== Statistical Randomness Tests ===")
print()
print("Sequence length:", len(bits))
print()
print("Frequency Test:")
print("  Ones: ", ones)
print("  Zeros:", zeros)
print()
print("Runs Test:")
print("  Total runs:", runs)
print()
print("Mean Value:", round(mean, 4))
print()
if 0.4 < mean < 0.6:
    print("Result: Sequence passes basic randomness tests")
else:
    print("Result: Sequence may not be random enough")
def weak_lfsr(seed, taps, steps):
    register = seed[:]
    output = []
    for _ in range(steps):
        feedback = 0
        for t in taps:
            feedback = feedback ^ register[t]
        output.append(register[-1])
        register = [feedback] + register[:-1]
    return output

weak_bits = weak_lfsr([1, 0], [0, 1], 20)
print("___ Weak Generator ___")
print("Register size: 2 bits")
print("Output:", weak_bits)
sequence = ''.join(map(str, weak_bits))
for p in range(1, 10):
    if sequence[:p] == sequence[p:2*p]:
        print("Period detected at:", p)
        break

print()

strong_bits = weak_lfsr([1, 0, 1, 1, 0, 1], [0, 5], 40)
print("___ Stronger Generator ___")
print("Register size: 6 bits")
print("Output:", strong_bits)
sequence2 = ''.join(map(str, strong_bits))
period_found = False
for p in range(1, 40):
    if sequence2[:p] == sequence2[p:2*p]:
        print("Period detected at:", p)
        period_found = True
        break
if not period_found:
    print("No short period found - harder to predict")

print()

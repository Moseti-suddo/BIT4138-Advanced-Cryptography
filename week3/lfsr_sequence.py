def lfsr(seed, taps, steps):
    register = seed[:]
    output = []

    for _ in range(steps):
        feedback = 0
        for t in taps:
            feedback = feedback ^ register[t]
        output.append(register[-1])
        register = [feedback] + register[:-1]

    return output

seed = [1, 0, 1, 1]
taps = [0, 3]

bits = lfsr(seed, taps, 100)

print("Generated sequence (100 bits):")
print(bits)
print()
print("Total bits generated:", len(bits))

# detect period by looking for repeating pattern
sequence_str = ''.join(map(str, bits))
period_found = False
for p in range(1, 50):
    if sequence_str[:p] == sequence_str[p:2*p]:
        print("Period detected:", p)
        period_found = True
        break

if not period_found:
    print("No short period detected - sequence looks good")
def lfsr(seed, taps, steps):
    register = seed[:]
    output = []

    for step in range(steps):
        print(f"Step {step + 1}: {register}")
        
        feedback = 0
        for t in taps:
            feedback = feedback ^ register[t]
        
        output.append(register[-1])
        register = [feedback] + register[:-1]

    return output

seed = [1, 0, 1, 1]
taps = [0, 3]

print("Seed:", seed)
print("Taps:", taps)
print()
bits = lfsr(seed, taps, 10)
print()
print("Output bits:", bits)
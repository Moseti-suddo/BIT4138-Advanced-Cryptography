def lfsr(seed, taps, steps):
    register = seed[:]
    output = []

    for _ in range(steps):
        print("Register state:", register)
        
        feedback = 0
        for t in taps:
            feedback = feedback ^ register[t]
        
        output.append(register[-1])
        register = [feedback] + register[:-1]
    
    return output

seed = [1, 0, 1, 1]
taps = [0, 3]
steps = 10

print("Starting LFSR")
print("Seed:", seed)
print("Taps:", taps)
print()
bits = lfsr(seed, taps, steps)
print()
print("Output sequence:", bits)
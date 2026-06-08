def berlekamp_massey(sequence):
    n = len(sequence)
    C = [1]
    B = [1]
    L = 0
    m = 1

    for i in range(n):
        d = sequence[i]
        for j in range(1, L + 1):
            d = d ^ (C[j] * sequence[i - j])
        d = d % 2

        if d == 0:
            m += 1
        elif 2 * L <= i:
            T = C[:]
            padding = [0] * m
            scaled = padding + B[:]
            while len(scaled) < len(C):
                scaled.append(0)
            while len(C) < len(scaled):
                C.append(0)
            C = [(C[k] ^ scaled[k]) % 2 for k in range(len(C))]
            L = i + 1 - L
            B = T[:]
            m = 1
        else:
            padding = [0] * m
            scaled = padding + B[:]
            while len(scaled) < len(C):
                scaled.append(0)
            while len(C) < len(scaled):
                C.append(0)
            C = [(C[k] ^ scaled[k]) % 2 for k in range(len(C))]
            m += 1

    return L

def analyse(name, sequence):
    L = berlekamp_massey(sequence)
    ratio = L / len(sequence)
    
    if ratio < 0.3:
        rating = "WEAK - easily cracked"
        fix = "Use longer register with better tap selection"
    elif ratio < 0.5:
        rating = "MODERATE - some risk"
        fix = "Add nonlinear components to improve security"
    else:
        rating = "ACCEPTABLE - harder to attack"
        fix = "Consider combining with nonlinear filter"

    print(f"Configuration: {name}")
    print(f"Sequence length: {len(sequence)}")
    print(f"Linear complexity: {L}")
    print(f"Complexity ratio: {round(ratio, 2)}")
    print(f"Security rating: {rating}")
    print(f"Recommendation: {fix}")
    print("-" * 50)

short =  [1, 0, 1, 0, 1, 0, 1, 0]
medium = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1]
high =   [1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1]

print("___ Stream Cipher Security Analysis Report ___")
print()
analyse("Short", short)
analyse("Medium", medium)
analyse("High", high)

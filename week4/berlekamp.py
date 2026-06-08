def berlekamp_massey(sequence):
    n = len(sequence)
    C = [1]
    B = [1]
    L = 0
    m = 1
    b = 1

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
            scaled = [x for x in B]
            scaled = padding + scaled
            while len(scaled) < len(C):
                scaled.append(0)
            while len(C) < len(scaled):
                C.append(0)
            C = [(C[k] ^ scaled[k]) % 2 for k in range(len(C))]
            L = i + 1 - L
            B = T[:]
            b = d
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

    return L, C

sequence = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1]

print("Input sequence:", sequence)
print()
L, poly = berlekamp_massey(sequence)
print("Linear complexity:", L)
print("Minimal polynomial:", poly)
print()
if L < len(sequence) / 2:
    print("Warning: low linear complexity, sequence is predictable")
else:
    print("Linear complexity looks acceptable")
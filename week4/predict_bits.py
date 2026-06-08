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
            scaled = padding + B[:]
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

def predict_next_bits(sequence, poly, L, steps):
    extended = sequence[:]
    for _ in range(steps):
        next_bit = 0
        for j in range(1, L + 1):
            if j < len(poly):
                next_bit = next_bit ^ (poly[j] * extended[-j])
        next_bit = next_bit % 2
        extended.append(next_bit)
    return extended[len(sequence):]

sequence = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1]

L, poly = berlekamp_massey(sequence)

print("Known sequence:", sequence)
print("Linear complexity:", L)
print("Recovered polynomial:", poly)
print()

predicted = predict_next_bits(sequence, poly, L, 8)
print("Predicted next 8 bits:", predicted)
print()
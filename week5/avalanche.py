def round_function(block, key):
    return block ^ key

def feistel_rounds(plaintext, keys):
    left = plaintext[:4]
    right = plaintext[4:]
    states = [left + right]
    for i in range(4):
        new_right = [left[j] ^ round_function(right[j], keys[i]) for j in range(4)]
        left = right
        right = new_right
        states.append(left + right)
    return states

def count_differences(block1, block2):
    return sum(1 for i in range(len(block1)) if block1[i] != block2[i])

keys = [3, 7, 5, 2]

original = [1, 0, 1, 1, 0, 1, 1, 0]
flipped =  [0, 0, 1, 1, 0, 1, 1, 0]

states1 = feistel_rounds(original, keys)
states2 = feistel_rounds(flipped, keys)

print("_" * 50)
print(f"{'Round':<10} {'Bit Differences':<20} {'Percentage'}")
print("_" * 50)

for i in range(len(states1)):
    diff = count_differences(states1[i], states2[i])
    percent = round((diff / len(states1[i])) * 100, 2)
    label = "Start" if i == 0 else str(i)
    print(f"{label:<10} {diff:<20} {percent}%")

print("_" * 50)
print()

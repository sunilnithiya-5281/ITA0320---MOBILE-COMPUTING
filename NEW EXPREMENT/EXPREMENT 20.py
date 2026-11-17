
# CDMA Spreading and Despreading

# Walsh-Hadamard matrix
codes = [
    [1, 1, 1, 1],
    [1, -1, 1, -1],
    [1, 1, -1, -1],
    [1, -1, -1, 1]
]

# Data of three users
users = [
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 0, 0]
]

# Convert bits into BPSK
symbols = []

for data in users:
    row = []
    for bit in data:
        if bit == 1:
            row.append(1)
        else:
            row.append(-1)
    symbols.append(row)

# Spreading
spread_signals = []

for i in range(3):
    signal = []
    for bit in symbols[i]:
        for chip in codes[i]:
            signal.append(bit * chip)
    spread_signals.append(signal)

# Composite signal
composite = []

for i in range(len(spread_signals[0])):
    total = 0
    for j in range(3):
        total += spread_signals[j][i]
    composite.append(total)

print("Composite Signal:")
print(composite)

# Despreading
print("\nRecovered Data:")

for i in range(3):
    recovered = []

    for j in range(4):
        total = 0
        for k in range(4):
            total += composite[j * 4 + k] * codes[i][k]

        result = total / 4

        if result > 0:
            recovered.append(1)
        else:
            recovered.append(0)

    print("User", i + 1, ":", recovered)
    print("Original Data:", users[i])

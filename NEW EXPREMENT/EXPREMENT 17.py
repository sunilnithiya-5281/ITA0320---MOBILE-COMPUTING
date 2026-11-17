
import math

# Given values
S = 420
M = 10
n = 4

# Generate valid cluster sizes
N_values = []

for i in range(0, 6):
    for j in range(0, 6):
        N = i*i + i*j + j*j

        if N > 0 and N not in N_values:
            N_values.append(N)

N_values.sort()

print("N\tQ\t\tChannels\tCapacity\tS/I (dB)")

for N in N_values:
    Q = math.sqrt(3 * N)

    k = math.floor(S / N)

    C = M * k * N

    SI = (Q ** n) / 6

    SI_dB = 10 * math.log10(SI)

    print(N, "\t", round(Q, 2), "\t",
          k, "\t\t", C, "\t\t", round(SI_dB, 2))

    if SI_dB >= 18:
        print("\nSmallest cluster size satisfying 18 dB =", N)
        break

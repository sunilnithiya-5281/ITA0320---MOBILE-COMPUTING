
import math
import matplotlib.pyplot as plt

# Erlang B function
def erlang_b(E, m):
    B = 1
    for k in range(1, m + 1):
        B = (E * B) / (k + E * B)
    return B

# Given values
traffic = [2, 5, 10, 20]
channels = [5, 10, 15, 20, 25, 30]

# Print table
print("Erlang B Blocking Probability")
print("Erlangs\tChannels\tBlocking Probability")

for E in traffic:
    for m in channels:
        B = erlang_b(E, m)
        print(E, "\t", m, "\t\t", round(B, 5))

# Find required channels
E = 10
GoS = 0.02
m = 1

while erlang_b(E, m) > GoS:
    m = m + 1

print("\nRequired number of channels =", m)
print("Blocking Probability =", round(erlang_b(E, m), 5))

# Plot graph
for E in traffic:
    values = []
    for m in channels:
        values.append(erlang_b(E, m))

    plt.plot(channels, values, marker='o', label=str(E) + " Erlangs")

plt.xlabel("Number of Channels")
plt.ylabel("Blocking Probability")
plt.title("Erlang B Formula")
plt.legend()
plt.grid()
plt.show()

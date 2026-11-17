
import numpy as np
import matplotlib.pyplot as plt

# Given values
U = 6
TTI = 2000
SNR = [25, 20, 15, 10, 5, 0]

snr = 10 ** (np.array(SNR) / 10)

np.random.seed(42)

# Generate channel gains
gain = np.random.exponential(1, (TTI, U))

# Calculate rate
rate = np.log2(1 + snr * gain)

# Jain's fairness index
def jain(x):
    return (sum(x) ** 2) / (U * sum(x ** 2))

# Round Robin
rr = np.zeros(U)

for t in range(TTI):
    user = t % U
    rr[user] += rate[t, user]

rr = rr / TTI

# Maximum C/I
mc = np.zeros(U)

for t in range(TTI):
    user = np.argmax(rate[t])
    mc[user] += rate[t, user]

mc = mc / TTI

# Proportional Fair
pf = np.zeros(U)
avg = np.ones(U) * 0.01

for t in range(TTI):
    score = rate[t] / avg
    user = np.argmax(score)

    pf[user] += rate[t, user]
    avg = 0.99 * avg
    avg[user] += 0.01 * rate[t, user]

pf = pf / TTI

# Print results
print("Scheduler\tTotal Throughput\tFairness")

for name, x in [("Round Robin", rr),
                ("Maximum C/I", mc),
                ("Proportional Fair", pf)]:

    print("\n", name)
    print("User Throughput:", np.round(x, 3))
    print("Total Throughput:", round(sum(x), 3))
    print("Jain's Index:", round(jain(x), 3))

# Plot throughput
users = range(1, U + 1)

plt.plot(users, rr, marker='o', label="Round Robin")
plt.plot(users, mc, marker='s', label="Maximum C/I")
plt.plot(users, pf, marker='^', label="Proportional Fair")

plt.xlabel("Users")
plt.ylabel("Throughput (bps/Hz)")
plt.title("OFDMA User Throughput")
plt.legend()
plt.grid()
plt.show()

# Fairness graph
names = ["Round Robin", "Maximum C/I", "Proportional Fair"]
fairness = [jain(rr), jain(mc), jain(pf)]

plt.bar(names, fairness)
plt.ylabel("Jain's Fairness Index")
plt.title("Scheduler Fairness Comparison")
plt.grid(axis='y')
plt.show()

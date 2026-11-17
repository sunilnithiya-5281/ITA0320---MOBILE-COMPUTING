
import math
import random
import matplotlib.pyplot as plt

# Given values
P0 = -30
n = 3.5
sigma = 4

# Mobile positions
positions = range(10, 2001, 5)

# Fixed random seed
random.seed(42)

# Calculate RSS values
rss1 = []
rss2 = []

for x in positions:
    d1 = max(x, 1)
    d2 = max(2000 - x, 1)

    s1 = random.gauss(0, sigma)
    s2 = random.gauss(0, sigma)

    r1 = P0 - 10 * n * math.log10(d1) + s1
    r2 = P0 - 10 * n * math.log10(d2) + s2

    rss1.append(r1)
    rss2.append(r2)

# Hysteresis values
H_values = [0, 2, 4, 6, 8, 10]

handoffs = []
pingpongs = []

# Simulation
for H in H_values:

    serving = 1
    count = 0

    for i in range(len(positions)):

        if serving == 1 and rss2[i] > rss1[i] + H:
            serving = 2
            count += 1

        elif serving == 2 and rss1[i] > rss2[i] + H:
            serving = 1
            count += 1

    ping = max(0, count - 1)

    handoffs.append(count)
    pingpongs.append(ping)

# Print results
print("Hysteresis\tHandoffs\tPing-Pong")

for i in range(len(H_values)):
    print(H_values[i], "\t\t", handoffs[i],
          "\t\t", pingpongs[i])

# Plot graph
plt.plot(H_values, handoffs, marker='o', label="Handoffs")
plt.plot(H_values, pingpongs, marker='s', label="Ping-Pong")

plt.xlabel("Hysteresis (dB)")
plt.ylabel("Number of Events")
plt.title("Handoff Simulation with Hysteresis")
plt.legend()
plt.grid()
plt.show()

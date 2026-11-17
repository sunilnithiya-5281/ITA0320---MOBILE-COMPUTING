
import numpy as np
import matplotlib.pyplot as plt

Pt = 30
Gt = 2
Gr = 2

distance = [0.1, 1, 2, 5, 10]
frequency = [900, 1800]

for f in frequency:
    fspl_list = []
    pr_list = []

    print("\nFrequency:", f, "MHz")
    print("Distance\tFSPL\tReceived Power\tPower(W)")

    for d in distance:
        L = 20*np.log10(d) + 20*np.log10(f) + 32.44

        Pr = Pt + Gt + Gr - L
        Pr_W = 10**(Pr/10)/1000

        fspl_list.append(L)
        pr_list.append(Pr)

        print(d, round(L, 2), round(Pr, 2), Pr_W)

    plt.plot(distance, fspl_list, marker='o', label=str(f)+" MHz")

plt.xlabel("Distance (km)")
plt.ylabel("FSPL (dB)")
plt.title("Free Space Path Loss")
plt.legend()
plt.grid()
plt.show()

for f in frequency:
    pr_list = []

    for d in distance:
        L = 20*np.log10(d) + 20*np.log10(f) + 32.44
        Pr = Pt + Gt + Gr - L
        pr_list.append(Pr)

    plt.plot(distance, pr_list, marker='o', label=str(f)+" MHz")

plt.xlabel("Distance (km)")
plt.ylabel("Received Power (dBm)")
plt.title("Received Power")
plt.legend()
plt.grid()
plt.show()

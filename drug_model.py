import math
import matplotlib.pyplot as plt
C0=25
k=0.2
times= []
concentrations = []
for t in range(6):
    C=C0*math.exp(-k*t)
    times.append(t)
    concentrations.append(C)
print(times)
print(concentrations)
plt.plot(times,concentrations)
plt.xlabel('time(hours)')
plt.ylabel('concentration')
plt.title('Drug Concentration vs time')
plt.show()
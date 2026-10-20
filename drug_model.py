"""
Drug Concentration Simulator

A beginner biomedical engineering project combining
Python, differential equations, and chemistry.

This program:
1. Models exponential drug concentration decay.
2. Converts mass concentration to molar concentration.
3. Calculates the rate of concentration change.
4. Uses Euler's method to approximate drug concentration.
5. Compares numerical and analytical solutions.
6. Calculates numerical error.

This is an educational simulation using hypothetical parameters,
not a model for clinical medication dosing.
"""
import math
import matplotlib.pyplot as plt

# Initial drug parameters
C0 = 25
k = 0.2
molar_mass = 200

# Create empty lists
times = []
concentrations = []
molar_concentrations = []
rates = []

# Calculate drug concentration over 10 hours
for t in range(11):
    C = C0 * math.exp(-k * t)
    rate = -k * C

    # Convert mg/L to mol/L and then micromolar
    M = C / (1000 * molar_mass)
    M_uM = M * 1000000

    # Store calculated values
    times.append(t)
    concentrations.append(C)
    molar_concentrations.append(M_uM)
    rates.append(rate)

# Check that all lists have 11 values
print("Times:", len(times))
print("Concentrations:", len(concentrations))
print("Molar concentrations:", len(molar_concentrations))
print("Rates:", len(rates))

# Create figure for three graphs
plt.figure(figsize=(8, 9))

# Graph 1: Mass concentration
plt.subplot(3, 1, 1)
plt.plot(times, concentrations)
plt.ylabel("Concentration (mg/L)")
plt.title("Drug Concentration Model")

# Graph 2: Molar concentration
plt.subplot(3, 1, 2)
plt.plot(times, molar_concentrations)
plt.ylabel("Concentration (uM)")

# Graph 3: Rate of change
plt.subplot(3, 1, 3)
plt.plot(times, rates)
plt.xlabel("Time (hours)")
plt.ylabel("Rate (mg/L/hour)")

# Adjust spacing and display graphs
plt.tight_layout()
plt.show()
# Euler's Method Simulation

C_euler = 25
dt = 1
k = 0.2

euler_times = [0]
euler_concentrations = [C_euler]

for step in range(20):
    C_euler = C_euler + dt * (-k * C_euler)

    euler_times.append((step + 1) * dt)
    euler_concentrations.append(C_euler)

print("Number of time values:", len(euler_times))
print("Number of concentrations:", len(euler_concentrations))
print("Final Euler concentration:", C_euler)
# Compare Euler's Method with Exact Solution

exact_concentrations = []

for t in euler_times:
    C_exact = C0 * math.exp(-k * t)
    exact_concentrations.append(C_exact)

plt.figure(figsize=(9, 5))

plt.plot(euler_times, exact_concentrations, label="Exact Solution")
plt.plot(euler_times, euler_concentrations, label="Euler's Method")

plt.xlabel("Time (hours)")
plt.ylabel("Concentration (mg/L)")
plt.title("Exact Solution vs Euler's Method")

plt.legend()
plt.grid(True)
plt.show()
# Calculate numerical error

exact_final = C0 * math.exp(-k * 10)

absolute_error = abs(exact_final - C_euler)

percent_error = (absolute_error / exact_final) * 100

print("Exact final concentration:", exact_final)
print("Euler final concentration:", C_euler)
print("Absolute error:", absolute_error)
print("Percent error:", percent_error)
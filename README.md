# drug-concentration-model
A biomedical engineering project combining differentiable equations,model drug concentration, differential equations, chemical kinetics, and biological systems through computational simulations and data visualization.
# Drug Concentration Simulator

## Project Overview

A biomedical engineering project combining differentiable equations
Chemistry to simulate drug concentration
changes over time.

This project uses differential equations, chemical
concentration conversions, and numerical methods to
model the elimination of a hypothetical drug from
a single compartment.

The simulation demonstrates how mathematical modeling
and programming can be applied to biomedical engineering.

## Project Objectives

- Model drug concentration using exponential decay.
- Apply differential equations to concentration changes.
- Convert mass concentration into molar concentration.
- Implement Euler's method for numerical approximation.
- Compare analytical and numerical solutions.
- Calculate numerical error.
- Visualize results using Python.

## Mathematical Model

The analytical solution is:

C(t) = C0 * e^(-kt)

Where:

- C(t) = Drug concentration at time t (mg/L)
- C0 = Initial concentration (25 mg/L)
- k = Elimination rate constant (0.2 per hour)
- t = Time (hours)

The corresponding differential equation is:

dC/dt = -kC

## Euler's Method

Euler's method approximates the differential equation
using small time steps.

C_next = C_current + dt * (-k * C_current)

Smaller time steps generally produce more accurate
approximations for this model.

## Chemistry Applications

The program converts drug concentration from mg/L
into mol/L and micromolar (uM).

A hypothetical molecular mass of 200 g/mol is used.

## Python Libraries

- math: Exponential calculations
- matplotlib: Data visualization

## Results

The program generates graphs displaying:

1. Drug concentration over time (mg/L)
2. Molar concentration over time (uM)
3. Rate of concentration change
4. Euler's method compared with the exact solution

The program also calculates the numerical error
between Euler's method and the analytical solution.

## How to Run

1. Install Python.
2. Install Matplotlib:

   python -m pip install matplotlib

3. Run the program:

   python drug_model.py

## Future Improvements

- Explore additional numerical methods.
- Model multiple compartments.
- Add interactive parameter inputs.
- Investigate more advanced pharmacokinetic models.

## Disclaimer

This project is an educational simulation using
hypothetical parameters. It is not intended for
clinical medication dosing or treatment decisions.
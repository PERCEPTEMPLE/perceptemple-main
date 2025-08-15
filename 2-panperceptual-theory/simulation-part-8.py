import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from scipy.integrate import quad # Although imported, it is not used directly in this script for PWF calculation.

# Observer parameters with PCI_T (Temporal Perceptual Complexity Index),
# F (Processing Frequency), S_T (Temporal Entropy), and SE_k (Standard Error of wavenumber k)
observers = {
    "Human": {"ICP_T": 9e11, "F": 40, "S_T": 0.8, "SE_k": 0.02},
    "Bat": {"ICP_T": 1.2e10, "F": 120, "S_T": 0.9, "SE_k": 0.01},
    "Octopus": {"ICP_T": 2.5e9, "F": 20, "S_T": 0.7, "SE_k": 0.02},
    "AI": {"ICP_T": 2.2e18, "F": 1e9, "S_T": 0.6, "SE_k": 0.03},
    "Shamanic": {"ICP_T": 3.3e12, "F": 150, "S_T": 0.85, "SE_k": 0.02},
    "Plant": {"ICP_T": 1.1e3, "F": 0.01, "S_T": 0.5, "SE_k": 0.05},
    "Quantum": {"ICP_T": 1e19, "F": 1e7, "S_T": 0.95, "SE_k": 0.01},
    "Cosmological": {"ICP_T": 1e30, "F": 1e10, "S_T": 1.0, "SE_k": 0.10}
}

# Spatial domain for the simulation of Perceptual Wave Functions (PWFs)
x = np.linspace(-10, 10, 1000)
t = 0 # Time is fixed at 0 to visualize the waveform at a given instant

# Figure setup for PWF visualization
plt.figure(figsize=(12, 8))

# Initialization of the emergent PWF. It is an array of complex numbers,
# initially filled with zeros, with the same shape as 'x'.
phi_emergent = np.zeros_like(x, dtype=complex)

# Dictionary to store the real parts of the simulated individual PWFs.
# This will be used to calculate correlations with the emergent PWF.
simulated_data = {}

# Normalization constant (kappa) used in the calculation of the wavenumber 'k'.
# It is set to 1e9 as specified in the paper.
kappa = 1e9

# Main loop to iterate over each defined observer
for obs, params in observers.items():
    # Calculate the wavenumber 'k' for the current observer.
    # The square root of PCI_T divided by kappa is used.
    k = np.sqrt(params["ICP_T"]) / kappa
    # The angular frequency 'omega' is simply the observer's frequency 'F'.
    omega = params["F"]
    # Calculate the Perceptual Wave Function (phi) for the observer.
    # It is a complex exponential e^(i * (k*x - omega*t)).
    phi = np.exp(1j * (k * x - omega * t))

    # Plot the real part of the current PWF.
    # The real part is chosen for visualization as PWFs are inherently complex.
    plt.plot(x, phi.real, label=obs)

    # Store the real part of the PWF in the dictionary for later correlation analysis.
    simulated_data[obs] = phi.real

    # Contribution to the emergent PWF.
    # The individual PWF and a simplified coupling term (0.3 * phi * phi) are added.
    # This quadratic term simulates a non-linear interaction between perceptions.
    phi_emergent += phi + 0.3 * phi * phi

# Normalize the emergent PWF so its values are in a comparable range to the individual PWFs.
# This is mainly for visualization purposes and does not affect correlations if the normalization is linear.
phi_emergent_normalized = phi_emergent / len(observers)

# Plot the real part of the normalized emergent PWF.
# A black dashed line ('k--') is used to distinguish it.
plt.plot(x, phi_emergent_normalized.real, "k--", label="Emergent PWF (Normalized)", linewidth=2)

# Print the correlations between each individual PWF and the normalized emergent PWF.
print("Correlations between Individual PWFs and Emergent PWF (Real Part):")
for obs, data in simulated_data.items():
    # Check if the standard deviation of the data is greater than zero to avoid errors
    # in the pearsonr function when the data is constant.
    if np.std(data) > 0 and np.std(phi_emergent_normalized.real) > 0:
        # Calculate the Pearson correlation coefficient (r) and the p-value.
        r, p = pearsonr(data, phi_emergent_normalized.real)
        # Print the coefficient of determination (R^2 = r^2) and the formatted p-value.
        print(f"  {obs}: R² = {r**2:.4f}, p-value = {p:.4f}")
    else:
        # Message if the correlation cannot be calculated.
        print(f"  {obs}: Cannot calculate R² (constant data or zero variance).")

# Configuration of the plot titles and labels.
plt.title("Individual and Emergent Perceptual Wave Functions (PWF)")
plt.xlabel("Spatial Domain (x)")
plt.ylabel("Real Amplitude of PWF")
plt.legend() # Display the legend with observer names
plt.grid(True) # Display a grid on the plot
plt.show() # Show the generated plot

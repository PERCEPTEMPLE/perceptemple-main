import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Definition of parameters for each observer type
# Each observer has a PCI_T (Temporal Perceptual Complexity Index),
# an F (Processing Frequency in Hz), S_T (Temporal Entropy),
# and SE_k (Standard Error of the wavenumber k for uncertainty in calculation)
observers = {
    "Human": {"ICP_T": 9e11, "F": 40, "S_T": 0.8, "SE_k": 0.02},
    "Bat": {"ICP_T": 1.2e10, "F": 120, "S_T": 0.9, "SE_k": 0.01},
    "Octopus": {"ICP_T": 2.5e9, "F": 20, "S_T": 0.7, "SE_k": 0.02},
    "AI": {"ICP_T": 2.2e18, "F": 1e9, "S_T": 0.6, "SE_k": 0.03},
    "Shamanic": {"ICP_T": 3.3e12, "F": 150, "S_T": 0.85, "SE_k": 0.02},
    "Plant": {"ICP_T": 1.1e3, "F": 0.01, "S_T": 0.5, "SE_k": 0.05},
    "Quantum": {"ICP_T": 1e19, "F": 1e7, "S_T": 0.95, "SE_k": 0.01},
    "Dream": {"ICP_T": 3.6e11, "F": 6, "S_T": 0.9, "SE_k": 0.03},
    "Simulation": {"ICP_T": 5e16, "F": 1e6, "S_T": 0.7, "SE_k": 0.02}
}

# Spatial domain for the simulation of Perceptual Wave Functions (PWF)
# A range of values from -10 to 10 is created, with 1000 points.
x = np.linspace(-10, 10, 1000)
t = 0 # Time is fixed at 0 to observe the waveform at a specific instant.

# Configuration of the figure and axes for the plot visualization
plt.figure(figsize=(12, 8))

# Initialization of the emergent PWF. It is an array of complex numbers
# that will accumulate the superposition of the individual PWFs.
phi_emergent = np.zeros_like(x, dtype=complex)

# Dictionary to store the real part of each simulated PWF.
# This is necessary to calculate correlations with the emergent PWF.
simulated_data = {}

# Normalization constant 'kappa' for the calculation of the wavenumber 'k'.
# The value 1e9 is used, as specified in the theoretical framework.
kappa = 1e9

# Main loop that iterates through each defined observer
for obs, params in observers.items():
    # Calculate the wavenumber 'k' for the current observer
    # k = sqrt(ICP_T) / kappa
    k = np.sqrt(params["ICP_T"]) / kappa
    # The angular frequency 'omega' is equal to the observer's frequency 'F'
    omega = params["F"]
    # Calculate the complex Perceptual Wave Function (phi) for the observer.
    # phi = e^(i * (k*x - omega*t))
    phi = np.exp(1j * (k * x - omega * t))

    # Plot the real part of the current PWF.
    # The real part is chosen for visualization, as the wave is complex.
    plt.plot(x, phi.real, label=obs)

    # Store the real part of the PWF in the 'simulated_data' dictionary.
    simulated_data[obs] = phi.real

    # Contribution to the emergent PWF.
    # The individual PWF (phi) and a non-linear coupling term (0.3 * phi * phi) are added.
    # This term simulates the interaction and co-construction of reality.
    phi_emergent += phi + 0.3 * phi * phi

# Plot the real part of the emergent PWF.
# A black dashed line ('k--') is used to highlight it.
plt.plot(x, phi_emergent.real, 'k--', label='Emergent PWF', linewidth=2)

# Loop to calculate and print the correlations between each individual PWF and the emergent PWF.
print("Correlations between Individual PWFs and Emergent PWF (Real Part):")
for obs, data in simulated_data.items():
    # It is verified that the data is not constant (variance > 0) to avoid errors in pearsonr.
    if np.std(data) > 0 and np.std(phi_emergent.real) > 0:
        # Calculate the Pearson correlation coefficient (r) and the p-value.
        r, p = pearsonr(data, phi_emergent.real)
        # Print the coefficient of determination (R^2 = r^2) and the formatted p-value.
        print(f"  {obs}: R^2={r**2:.4f}, p-value={p:.4f}")
    else:
        # Message in case the correlation cannot be calculated.
        print(f"  {obs}: Cannot calculate R^2 (constant data or zero variance).")

# Final configuration of the plot: title, axis labels, legend, and grid.
plt.title("Individual and Emergent Perceptual Wave Functions (PWF)")
plt.xlabel("Spatial Domain (x)")
plt.ylabel("Real Amplitude of PWF")
plt.legend() # Displays the legend to identify each line
plt.grid(True) # Activates the background grid
plt.savefig("superposition_fop.png") # Saves the plot as a PNG file
plt.show() # Displays the plot on the screen

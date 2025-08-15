import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Observers with their empirically derived parameters
observers = {
    "Human": {"PCI": 8e11, "F": 40, "SE_k": 0.02, "SE_F": 5},
    "Bat": {"PCI": 1.07e10, "F": 120, "SE_k": 0.01, "SE_F": 10},
    "Octopus": {"PCI": 2.33e9, "F": 20, "SE_k": 0.02, "SE_F": 3},
    "AI": {"PCI": 2e18, "F": 1e9, "SE_k": 0.03, "SE_F": 1e8},
    "Shamanic": {"PCI": 3e12, "F": 150, "SE_k": 0.02, "SE_F": 15},
    "Plant": {"PCI": 1e3, "F": 0.01, "SE_k": 0.05, "SE_F": 0.005},
    "Quantum": {"PCI": 9e18, "F": 1e7, "SE_k": 0.01, "SE_F": 2e6}
}

# Spatial domain for PWF simulation
x = np.linspace(-10, 10, 1000)
t = 0 # We consider time at a fixed instant for visualization

# Create figure to plot individual and emergent PWFs
plt.figure(figsize=(12, 8))
psi_emergent = np.zeros_like(x, dtype=complex) # Initialize the emergent PWF as complex zero
simulated_data = {} # Dictionary to store the real data of each simulated PWF

# Simulate the PWF for each observer and plot
kappa = 1e9 # Normalization constant for k
for obs, params in observers.items():
    k = np.sqrt(params["PCI"]) / kappa # Calculation of the wavenumber k
    omega = params["F"] # Angular frequency is equal to the processing frequency F
    psi = np.exp(1j * (k * x - omega * t)) # Calculation of the complex PWF
    plt.plot(x, psi.real, label=obs) # Plot only the real part of the PWF
    simulated_data[obs] = psi.real # Store the real part for correlation calculations
    psi_emergent += psi # Sum the individual PWFs for superposition

# Normalize the emergent PWF for better visualization if necessary
# This is not explicitly in formula (3) but can be useful for plotting
psi_emergent_normalized = psi_emergent / len(observers) # Simple normalization for visualization

# Plot the emergent function (real part)
plt.plot(x, psi_emergent_normalized.real, "k--", label="Emergent (Normalized)", linewidth=2)

# Calculate correlations between each individual PWF and the emergent PWF
print("\nCorrelations between Individual PWFs and Emergent PWF (Real Part):")
for obs, data in simulated_data.items():
    # Ensure arrays are not constant to calculate Pearsonr
    if np.std(data) > 0 and np.std(psi_emergent_normalized.real) > 0:
        r, p = pearsonr(data, psi_emergent_normalized.real)
        print(f"  {obs}: R² = {r**2:.4f}, p-value = {p:.4f}")
    else:
        print(f"  {obs}: Cannot calculate R² (constant data or zero variance).")

# Configure and display the plot
plt.title("Individual and Emergent Perceptual Wave Functions (PWF)")
plt.xlabel("Spatial Domain (x)")
plt.ylabel("Real Amplitude of PWF")
plt.legend()
plt.grid(True)
plt.show()

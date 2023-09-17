
import numpy as np
import time

# Parameters
S0 = 100
K = 100
r = 0.05
sigma = 0.2
T = 1
N = 100000
dt = 1/365  # assuming daily steps

# Monte Carlo simulation for European Call option
def monte_carlo_simulation(S0, K, r, sigma, T, N):
    # Simulate stock price paths
    Z = np.random.randn(N)
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    
    # Calculate payoffs
    payoffs = np.maximum(ST - K, 0)
    
    # Discounted expected payoff
    option_price = np.exp(-r * T) * np.mean(payoffs)
    
    return option_price

# Measure the time for Python
start_time_python = time.time()
option_price_python = monte_carlo_simulation(S0, K, r, sigma, T, N)
end_time_python = time.time()

execution_time_python = end_time_python - start_time_python
print(f"European Call Option Price: {option_price_python:.2f}")
print(f"Execution Time (Python): {execution_time_python:.4f} seconds")


using Random, Distributions, Statistics

# Parameters
S0 = 100
K = 100
r = 0.05
σ = 0.2
T = 1
N = 100000

function monte_carlo_simulation(S0, K, r, σ, T, N)
    Z = rand(Normal(0, 1), N)
    ST = S0 .* exp.((r - 0.5 * σ^2) * T .+ σ * sqrt(T) * Z)
    
    payoffs = max.(ST .- K, 0)
    option_price = exp(-r * T) * mean(payoffs)
    
    return option_price
end

# Compute and print the option price
option_price_julia = monte_carlo_simulation(S0, K, r, σ, T, N)
println("European Call Option Price: ", option_price_julia)

# Measure the time for Julia
@time monte_carlo_simulation(S0, K, r, σ, T, N)

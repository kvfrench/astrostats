#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 23:17:30 2025

@author: kfrench
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

#Parameters for questions 1 and 2
n = 100  # Number of trials
p = 0.4  # Probability of success
q = 1 - p  # Complement probability
num_experiments = 10000  # Number of experiments

# Simulate binomial experiments
samples = np.random.binomial(n, p, num_experiments)

# Compute histogram for empirical P(k)
k_values, counts = np.unique(samples, return_counts=True)
empirical_p_k = counts / num_experiments

# Compute theoretical P(k)
k_range = np.arange(0, n+1)
theoretical_p_k = binom.pmf(k_range, n, p)

# Compute normal approximation
mu = n * p
sigma = np.sqrt(n * p * q)
normal_approximation = (1 / np.sqrt(2 * np.pi * sigma**2)) * np.exp(-((k_range - mu) ** 2) / (2 * sigma**2))

# Plot 1
plt.figure(figsize=(10, 6))
plt.bar(k_values, empirical_p_k, alpha=0.6, color='blue', label='Empirical P(k)')
plt.plot(k_range, theoretical_p_k, 'r-', label='Theoretical P(k)', linewidth=2)
plt.plot(k_range, normal_approximation, 'g--', label='Normal Approximation', linewidth=2)
plt.xlabel('k (Number of successes)')
plt.ylabel('Probability(k)')
plt.title(f'Binomial Distribution: n={n}, p={p}, {num_experiments} Experiments')
plt.legend()
plt.grid()
plt.show()

#Parameters for question 3
n = 100  # Number of trials
p_base = 0.4  # Base probability of success
p_adjusted = 0.44  # Adjusted probability after two successes
num_experiments = 10000  # Number of experiments


# Function to simulate an experiment with adaptive p
def simulate_experiment(n, p_base, p_adjusted):
    experiment = np.zeros(n, dtype=int)  
    
 
    experiment[0] = np.random.rand() < p_base
    experiment[1] = np.random.rand() < p_base

    for i in range(2, n):
        
        if experiment[i - 1] == 1 and experiment[i - 2] == 1:
            p = p_adjusted 
        else:
            p = p_base  
        
        # Perform trial
        experiment[i] = np.random.rand() < p
    
    return np.sum(experiment)  

# Run experiments
adaptive_samples = np.array([simulate_experiment(n, p_base, p_adjusted) for _ in range(num_experiments)])

# Compute histogram for empirical P(k) with adaptive probability
k_values_adaptive, counts_adaptive = np.unique(adaptive_samples, return_counts=True)
empirical_p_k_adaptive = counts_adaptive / num_experiments

# Plot 2
plt.figure(figsize=(10, 6))
plt.bar(k_values_adaptive, empirical_p_k_adaptive, alpha=0.6, color='purple', label='Empirical P(k) (Adaptive)', width=0.8)
plt.bar(k_values, empirical_p_k, alpha=0.6, color='blue', label='Empirical P(k) (Fixed p)', width=0.8)
plt.plot(k_range, theoretical_p_k, 'r-', label='Theoretical P(k)', linewidth=2)
plt.plot(k_range, normal_approximation, 'g--', label='Normal Approximation', linewidth=2)
plt.xlabel('k (Number of successes)')
plt.ylabel('Probability(k)')
plt.title(f'Binomial Distribution with Adaptive p: n={n}, p={p_base}, {num_experiments} Experiments')
plt.legend()
plt.grid()
plt.show()
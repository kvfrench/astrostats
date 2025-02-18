#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:46:34 2025

@author: kfrench
"""

import numpy as np
import matplotlib.pyplot as plt

n = 100  # Sample size
mu = 0   # Population mean
sigma = 1  # Population standard deviation
trials = 10000

# Draw n samples from a Gaussian distribution
samples = np.random.normal(mu, sigma, n)

sample_mean = np.mean(samples)
print(f"Sample Mean X̄ from n samples: {sample_mean:.4f}")

sample_mean2 = np.array([np.mean(np.random.normal(mu, sigma, n)) for _ in range(trials)])

# Calculating what fraction of the 10,000 X̄ were in the range [−0.01,0.01]
range_min = -0.01
range_max = 0.01

count_in_range = np.sum((range_min <= sample_mean2) & (sample_mean2 <= range_max))

fraction_in_range = count_in_range / trials
print("Fraction of X̄ in the range [-0.01,0.01]:", fraction_in_range)

n_values = [10, 50, 100, 500, 1000, 5000]  # Different sample sizes
fractions = []

# Run the experiment for each n
for n in n_values:
    sample_mean2 = np.array([np.mean(np.random.normal(mu, sigma, n)) for _ in range(trials)])
    count_in_range = np.sum((range_min <= sample_mean2) & (sample_mean2 <= range_max))
    fraction = count_in_range / trials
    fractions.append(fraction)

# Plot the results
plt.figure(figsize=(8, 5))
plt.plot(n_values, fractions, marker='o', linestyle='-')
plt.xlabel("Sample Size (n)")
plt.ylabel("Fraction in [-0.01, 0.01]")
plt.title("Fraction of Sample Means in [-0.01, 0.01] vs. Sample Size")
plt.xscale("log")  # Use a log scale for better visualization
plt.grid()
plt.show()

# Good to see use of symbols in comments. Can also use in plots. Use either
# Unicode symbol like in comments or matplotlib's 'mathtext', e.g., $\epsilon$
# For n=100, determine the range [−ϵ,ϵ] for which 99% of the sample means fall in
n = 100
sample_mean3 = np.array([np.mean(np.random.normal(mu, sigma, n)) for _ in range(trials)])

# Calculate the 99% confidence interval 
lower_percentile = np.percentile(sample_mean3, 0.5)   
upper_percentile = np.percentile(sample_mean3, 99.5)  

# Calculate epsilon 
epsilon = (upper_percentile - lower_percentile) / 2

print(f"For n={n}, the range [-{epsilon:.4f}, {epsilon:.4f}] contains 99% of the sample means.")

# How does epsilon depend on n?
n_values = [10, 50, 100, 500, 1000]
epsilon_values = []

for n in n_values:
    sample_mean4 = np.array([np.mean(np.random.normal(mu, sigma, n)) for _ in range(trials)])
    lower_percentile = np.percentile(sample_mean4, 0.5)
    upper_percentile = np.percentile(sample_mean4, 99.5)
    epsilon = (upper_percentile - lower_percentile) / 2
    epsilon_values.append(epsilon)

# Plot epsilon vs. n
plt.figure(figsize=(8, 5))
plt.plot(n_values, epsilon_values, marker='o', linestyle='-', color='b')
plt.xlabel("Sample Size (n)")
plt.ylabel("Epsilon (half-width of 99% CI)")
plt.title("Epsilon vs. Sample Size (n)")
plt.xscale('log')
plt.yscale('log')  
plt.grid(True)
plt.show()


# Use uniform distribution instead of Gaussian
sample_mean_uniform = np.array([np.mean(np.random.uniform(-1, 1, n)) for _ in range(trials)])

# Calculate the 99% confidence interval (percentiles) for uniform distribution
lower_percentile_uniform = np.percentile(sample_mean_uniform, 0.5)
upper_percentile_uniform = np.percentile(sample_mean_uniform, 99.5)

# Calculate epsilon for uniform distribution
epsilon_uniform = (upper_percentile_uniform - lower_percentile_uniform) / 2

print(f"For uniform distribution (n={n}), the range [-{epsilon_uniform:.4f}, {epsilon_uniform:.4f}] contains 99% of the sample means.")

# Compare epsilon for different distributions
print(f"Ratio of epsilon (Uniform / Gaussian) for n={n}: {epsilon_uniform / epsilon:.4f}")



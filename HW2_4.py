#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:00:08 2025

@author: kfrench
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


population_mean = 5  #mean
population_std = 2    #standard deviation of population
n =   10          #Sample size
num_trials = 10000   #number of trials

# Generate a non-Gaussian population (Trying a uniform distribution)
lower_bound = 0
upper_bound = 10
population = np.random.uniform(low = lower_bound, high = upper_bound, size=100000)

# Draw samples and compute sample means
sample_mean = [np.mean(np.random.choice(population, size=n, replace=True)) for _ in range(num_trials)]

# Expected mean and standard deviation from CLT
expected_mean = population_mean
expected_std = population_std / np.sqrt(n)

# 95% Confidence Interval
lower_bound = expected_mean - 1.96 * expected_std
upper_bound = expected_mean + 1.96 * expected_std

# Plot histogram of sample means
plt.figure(figsize=(12, 5))
plt.hist(sample_mean, bins=50, density=True, alpha=0.6, color='b', label="Histogram of Samples")

# Overlay a Gaussian curve from CLT
x_values = np.linspace(min(sample_mean), max(sample_mean), 100)
plt.plot(x_values, norm.pdf(x_values, expected_mean, expected_std), 'r', lw=2, label="Central Limit Theorem Predicted Gaussian")

# Add confidence interval lines
plt.axvline(lower_bound, color='g', linestyle='dashed', label="95% CI Bounds")
plt.axvline(upper_bound, color='g', linestyle='dashed')

# Labels and legend
plt.axvline(expected_mean, color='black', linestyle='dotted', label="Population Mean (μ)")
plt.title("Demonstration of the Central Limit Theorem, Sample Size = 10")
plt.xlabel("Sample Mean")
plt.ylabel("Density")
plt.legend()
plt.grid()
plt.show()

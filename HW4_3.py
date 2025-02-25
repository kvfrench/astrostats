#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:28:09 2025

@author: kfrench
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, binom

# Load data
data = np.loadtxt("xray.txt")
dates = data[:, :3]  # Extract year, month, day

# Flare counts
unique_days, counts = np.unique(dates, axis=0, return_counts=True)

# Compute PDF 
unique_counts, frequencies = np.unique(counts, return_counts=True)
pdf = frequencies / np.sum(frequencies)  # Normalize PDF

# Compute λ 
lambda_poisson = np.mean(counts)

# Compute Poisson probabilities
poisson_prob = poisson.pmf(unique_counts, lambda_poisson)

# Estimate Binomial Parameters
n_max_counts = max(counts)  # Maximum observed flares per day 
est_prob = np.sum(counts) / (len(counts) * n_max_counts)  # Estimated probability of a flare occurring per trial

# Compute Binomial probabilities
binomial_prob = binom.pmf(unique_counts, n_max_counts, est_prob)

# Plot the PDF, Poisson, and Binomial distributions
plt.figure(figsize=(8, 5))
plt.bar(unique_counts, pdf, width=0.8, color="skyblue", edgecolor="black", label="Empirical PDF")
plt.plot(unique_counts, poisson_prob, color = 'red', markersize=5, label=f"Poisson (λ={lambda_poisson:.2f})")
plt.plot(unique_counts, binomial_prob, color='darkblue', markersize=5,label=f"Binomial (n={n_max_counts}, p={est_prob:.3f})")
plt.xlabel("Number of Solar Flares per Day")
plt.ylabel("Probability")
plt.title("Solar Flare Data \nEmpirical PDF vs. Poisson and Binomial Distributions")
plt.xticks(range(min(unique_counts), max(unique_counts) + 1))
plt.grid()
plt.legend()

plt.show()


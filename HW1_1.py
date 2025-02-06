#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 21:43:30 2025

@author: kfrench
"""

import random
import matplotlib.pyplot as plt

a = [0, 1] #list of possible outcomes

n_values = range(1, 1001)  # n from 1 to 1000
rf_zeros = []  # Relative frequency of 0
rf_ones = []   # Relative frequency of 1

# Experiment: Randomly select an element from the list a
result = random.choice(a)

# Run the experiment for each n value
for n in n_values:
    results = [random.choice(a) for _ in range(n)]  # Generate n random choices
    rf_zeros.append(results.count(0) / n)  # Compute relative frequency of 0
    rf_ones.append(results.count(1) / n)   # Compute relative frequency of 1


# Plot rf(0) and rf(1) vs n
plt.plot(n_values, rf_zeros, label="rf(0)", color="blue")
plt.plot(n_values, rf_ones, label="rf(1)", color="indianred")
plt.xlabel("Number of experiments (n)")
plt.ylabel("Relative frequency")
plt.title("Relative Frequency of 0 and 1 vs. Number of Experiments")
plt.legend()
plt.grid()
plt.show()


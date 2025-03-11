#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 15:46:28 2025

@author: kfrench
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#Given p-value and significance level
p_value = 0.0047
alpha = 0.05

#Calculate Z-score for the p-value 
Z = norm.ppf(1 - p_value / 2)

#Generate the normal distribution 
µ = 2  # Null hypothesis value
sigma = 0.1 # Assume population standard deviation
x = np.linspace(1.5, 2.5, 100)
y = norm.pdf(x, µ, sigma)

#Plot
plt.plot(x, y, label="Normal Distribution (H₀: μ = 2)")
plt.fill_between(x, y, where=(x > µ + Z * (sigma / np.sqrt(30))), color='red', alpha=0.5, label="P-value Area")
plt.fill_between(x, y, where=(x < µ - Z * (sigma / np.sqrt(30))), color='red', alpha=0.5)
plt.axvline(µ, color='green', linestyle='--', label=f"H₀: μ = {µ}")
plt.axvline(µ + Z * (sigma / np.sqrt(30)), color='black', linestyle='--', label=f"Z = {Z:.2f}")
plt.axvline(µ - Z * (sigma / np.sqrt(30)), color='black', linestyle='--', label=f"Z = {-Z:.2f}")
plt.title(f"Visualizing Test Statistic with P-value = {p_value}")
plt.xlabel("Sample Mean (μ)")
plt.ylabel("Density")
plt.legend()
plt.grid()
plt.show()


print(f"Z = {Z:.2f}, corresponding to P-value: {p_value}")


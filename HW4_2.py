#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:41:39 2025

@author: kfrench
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 23:23:58 2025

@author: kfrench
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

# Draw a sample of 10 values 
np.random.seed(42)  
n = 10  
gauss_dist = np.random.normal(loc=0, scale=1, size=n)

# Compute sample variance S^2 (unbiased estimate)
sample_var = np.var(gauss_dist, ddof=1)

# Bootstrap resampling
num_bootstrap_samples = 10000  
bootstrap_values = []

for _ in range(num_bootstrap_samples):
    bootstrap_sample = np.random.choice(gauss_dist, size=n, replace=True)  # Resample with replacement
    bootstrap_sample_var = np.var(bootstrap_sample, ddof=1)  # Compute sample variance for bootstrap sample
    bootstrap_values.append(bootstrap_sample_var)

bootstrap_values = np.array(bootstrap_values)

# Compute mean and variance of bootstrap sample variances
mean_bootstrap = np.mean(bootstrap_values)
var_bootstrap = np.var(bootstrap_values, ddof=1)

# Compute the exact mean and variance of the sampling distribution
exact_mean = 1  # E[S^2] = σ^2 = 1
exact_variance = 2 / (n - 1)  # Var(S^2) = 2σ^4 / (n-1)

# Generate theoretical gamma distribution
alpha = (n - 1) / 2  # Shape parameter
beta = 2 / (n - 1)   # Scale parameter

x = np.linspace(min(bootstrap_values), max(bootstrap_values), 200)
gamma_pdf = gamma.pdf(x, a=alpha, scale=beta)  

plt.figure(figsize=(8, 5))
plt.hist(bootstrap_values, bins=50, density=True, color='lightblue', edgecolor='black', label='Bootstrap PDF', alpha=0.7)
plt.plot(x, gamma_pdf, 'r-', label='Theoretical Gamma PDF')  
plt.axvline(sample_var, color='red', linestyle='dashed', linewidth=2, label=f'Original S² = {sample_var:.3f}')
plt.axvline(var_bootstrap, color='gray', linestyle='-', linewidth=2, label=f'Bootstrap Variance = {var_bootstrap:.3f}')
plt.axvline(mean_bootstrap, color='purple', linestyle=':', linewidth=2, label=f'Bootstrap Mean = {mean_bootstrap:.3f}')
plt.xlabel('S² (Sample Variance)')
plt.ylabel('Probability Density')
plt.title(f'Bootstrap & Theoretical Distribution of S²\n'
          f'Mean: Bootstrap = {mean_bootstrap:.3f}, Exact = {exact_mean:.3f} | '
          f'Variance: Bootstrap = {var_bootstrap:.3f}, Exact = {exact_variance:.3f}')
plt.legend()
plt.grid()
plt.show()

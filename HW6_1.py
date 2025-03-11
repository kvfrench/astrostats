#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 17:47:52 2025

@author: kfrench
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 20:39:50 2025

@author: kfrench
"""

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

#Given parameters
n = 100
µ = 2  # Null hypothesis 
var = 2   # Given variance
sigma = np.sqrt(var)  # Population standard deviation

#Generate Gaussian sample
random_gauss = np.random.normal(loc=µ, scale=sigma, size=n)

#Sample statistics
xbar = np.mean(random_gauss)
s_pop = np.std(random_gauss, ddof=0)  # Population standard deviation
s_sample = np.std(random_gauss, ddof=1)  # Sample standard deviation

#Compute test statistic (Z-score)
standard_error = sigma / np.sqrt(n)
z_score = (xbar - µ) / standard_error

#Compute 95% Confidence Interval for μ
alpha = 0.05
z_value = stats.norm.ppf(1 - alpha / 2)  # 1.96 for 95% CI


lower_ci = xbar - z_value * standard_error
upper_ci = xbar + z_value * standard_error


#Critical value for α = 0.05 
z_critical = 1.96  # For the 95% confidence level

#Decision based on the critical value method
reject_H0 = abs(z_score) > z_critical

# Print results
print(f"Standard Error: {standard_error:.4f}")
print(f"Sample mean: {xbar:.4f}")
print(f"Z-score: {z_score:.4f}")
print(f"Critical value: ±{z_critical}")
print("Conclusion: Reject H0" if reject_H0 else "Conclusion: Do not reject H0")

#Plot
plt.hist(random_gauss, bins=15, density=True, alpha=0.6, color='skyblue', zorder=1)
x = np.linspace(min(random_gauss), max(random_gauss), 100) 
pdf = stats.norm.pdf(x, loc=µ, scale=sigma) # Theoretical PDF
plt.plot(x, pdf, color='indianred', lw=2, zorder=2, label="PDF")
plt.axvline(xbar, color='black', linestyle='solid', linewidth=2, label=f'Mean = {xbar:.2f}')
plt.axvline(lower_ci, color='red', linestyle='dashed', linewidth=2, label=f'95% CI Lower = {lower_ci:.2f}')
plt.axvline(upper_ci, color='red', linestyle='dashed', linewidth=2, label=f'95% CI Upper = {upper_ci:.2f}')
plt.fill_between(x, pdf, where=(x < lower_ci) | (x > upper_ci), color='red', alpha=0.3, label="Rejection Region")
plt.xlabel("Gaussian Sample")
plt.ylabel("Probability Density")
plt.title("Rejection Region Test with Gaussian Distribution Sample")
plt.legend()
plt.grid(zorder=0)
plt.show()
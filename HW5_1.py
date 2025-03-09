#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:06:08 2025

@author: kfrench
"""

import numpy as np
import scipy.stats as stats

dev_vals = [1470, 1510, 1690, 1740, 1900, 2000, 2030, 2100, 2190, 2200, 2290, 2380, 2390, 2480, 2500, 2580, 2700]

#stats of values from Devore
dev_var = np.var(dev_vals, ddof =1) 
dev_mean = np.mean(dev_vals)
dev_stdev = np.std(dev_vals)


num_samples = 10000 #sample for bootstrapping
variance_array = [] #empty array for bootstrapping output

#bootstrapping for loop
for i in range(num_samples):
    boot_sampling = np.random.choice(dev_vals, size = len(dev_vals), replace = True)
    variance_array.append(np.var(boot_sampling, ddof=1))

#calculate 95% confidence interval
lower_CI = np.percentile(variance_array, 2.75)
upper_CI = np.percentile(variance_array, 97.5)

print(f"95% CI for σ², using bootstrapping of 17 samples: ({lower_CI:.0f}, {upper_CI:.0f})")

#create 100 values with same variance and mean as the Devore values, using gaussian distribution
large_sample = 100
large_vals = np.random.normal(loc=dev_mean, scale=dev_stdev, size=large_sample)

num_samples2 = 10000 #sample for bootstrapping
variance_array2 = [] #empty array for bootstrapping output

#bootstrapping of large Gaussian sample
# Try writing w/o loop.
for i in range(num_samples2):
    boot_sampling2 = np.random.choice(large_vals, size = len(large_vals), replace = True)
    variance_array2.append(np.var(boot_sampling2, ddof=1))
    


#Devore confidence interval method

# Defining degrees of freedom
n = len(large_vals)
df = n - 1

#getting mean of variances from bootstrapping, for use in Devore's approach
boot_var_mean = np.mean(variance_array2)

#Devore uses a chi-squared approach in 7.15
chi2_lower = stats.chi2.ppf(0.025, df)  
chi2_upper = stats.chi2.ppf(0.975, df)  

#Compute confidence interval for variance
lower_CI2 = (df * boot_var_mean) / chi2_upper
upper_CI2 = (df * boot_var_mean) / chi2_lower

# Print results
# Not really Devore's method. Is called "standard bootstrap CI".
# Other approach is "bootstrap percentile CI"
# (I didn't give details about this).
print(f"95% CI for σ², using Devore's method': ({lower_CI2:.0f}, {upper_CI2:.0f})")


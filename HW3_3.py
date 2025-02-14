#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 19:46:33 2025

@author: kfrench
"""

import numpy as np
import matplotlib.pyplot as plt

n= 10
mu = 0
sigma = 1
num_trials = 10000

sb_trials = []

for i in range(num_trials):
    norm_dist = np.random.normal(mu,sigma,n)   
    sb_form = np.sum((norm_dist - np.mean(norm_dist))**2) / n
    sb_trials.append(sb_form)

avg_sb = np.mean(sb_trials)
var_sb = np.var(sb_trials)

plt.hist(sb_trials, bins=50, color='blue', edgecolor='black')
#including the True variance to demonstrate that the variance from the trials is underestimating the population
plt.axvline(x=sigma**2, color='red', linestyle='dashed', label="True Variance = 1") 
plt.axvline(x=var_sb, color='purple', linestyle='dashed', label=f"Biased Variance = {var_sb:.4f}") 
plt.title(f"Histogram of $S_b^2$ (biased variance)\nMean: {avg_sb:.4f}, Variance: {var_sb:.4f}")
plt.xlabel("$S_b^2$")
plt.ylabel("Frequency")
plt.legend()
plt.grid()
plt.show()
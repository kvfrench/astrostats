#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:31:21 2025

@author: kfrench

Problem from SJSU 
https://www.sjsu.edu/people/steven.macramalla/courses/stats95/lecture%208%20--%20Confidence%20intervals%20FX%20Power%20Significance.pdf

According to the 2003-2004 annual report of the Association of Medical
and Graduate Departments of Biochemistry, the average stipend for a
postdoctoral trainee in biochemistry was $31,331 with a standard
deviation of $3,942. Treating this as the population, assume that you asked
the 8 biochemistry postdoctoral trainees at your institution what their
annual stipend was and that it averaged $34,000.


"""

import numpy as np
from scipy.stats import norm

n = 8 #trainees at institution
mu = 31331 #average stipend according to the annual report
sigma = 3942 #standard deviatoin
M = 34000 #average stipend of 8 sample population 
alpha = 0.05 #for the 95% confidence interval

#Calculating the z-statistics for this setup
z_critical = norm.ppf(1 - alpha/2)

# Standard error
std_error = sigma / np.sqrt(n)

# Confidence interval
lower_CI = M - z_critical * std_error
upper_CI = M + z_critical * std_error

print(f"95% CI for the mean stipend: (${lower_CI:.2f}, ${upper_CI:.2f})")

#bootstraping for confidence interval

num_samples = 10000 #samples for bootstrapping
means_array = [] #empty array for bootstrapping output

#constructing a distribution with the same statistics as the trainees

large_sample =100
pay_distro = np.random.normal(loc=M, scale=sigma, size=large_sample)

#bootstrapping for loop
for i in range(num_samples):
    boot_sampling = np.random.choice(pay_distro, size = len(pay_distro), replace = True)
    means_array.append(np.mean(boot_sampling))

#calculate 95% confidence interval
lower_CI = np.percentile(means_array, 2.75)
upper_CI = np.percentile(means_array, 97.5)

print(f"95% CI for σ², using bootstrapping of 100 samples: (${lower_CI:.2f}, ${upper_CI:.2f})")


#And just to see the difference in values, here's a verison with the sample population of 8

sample_pop = 8
pay_distro2 = np.random.normal(loc=M, scale=sigma, size=sample_pop)

means_array2 = []

#bootstrapping for loop
for i in range(num_samples):
    boot_sampling2 = np.random.choice(pay_distro2, size = len(pay_distro2), replace = True)
    means_array2.append(np.mean(boot_sampling2))

#calculate 95% confidence interval
lower_CI2 = np.percentile(means_array2, 2.75)
upper_CI2 = np.percentile(means_array2, 97.5)


print(f"95% CI for σ², using bootstrapping of 8 samples: (${lower_CI2:.2f}, ${upper_CI2:.2f})")

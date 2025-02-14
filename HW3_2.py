#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:25:07 2025

@author: kfrench
"""

"""

Use a random number generator to create a dataset that simulates the following result. 
Every hour, the number of x-ray flares is tabulated. 
It is found that over 1,000 days, 900 flares occurred so that the average probability of a flare 
in a given hour is 900/(1000⋅24).

"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

days = 1000
hours = 24
total_hours = days * hours
hourly_flare_rate = 900 / total_hours  # Expected rate of flares per hour

#Simulated dataset
flare_counts = np.random.poisson(lam=hourly_flare_rate, size=total_hours)

#Probability of k flare events occurring per day for the Simulated dataset
daily_flare_rate = flare_counts.reshape(days, hours).sum(axis=1)

#Calculate lambda for poisson distribution
lambda_daily = hours * hourly_flare_rate

#range of possible daily flares
k_values = np.arange(0, max(daily_flare_rate) + 1)

#Poisson pmf
poisson_p = stats.poisson.pmf(k_values, mu=lambda_daily)

#Binomial pmf
binomial_p = stats.binom.pmf(k_values, hours, hourly_flare_rate)


#Plot histogram of simulated data
plt.hist(daily_flare_rate, bins=range(0, max(daily_flare_rate) + 2), density=True, alpha=0.75, edgecolor='black', label="Simulated Data $P_s(k)$")

# Overlay Poisson distribution
plt.plot(k_values, poisson_p, 'ro-', markersize=5, label=r"Poisson $P_p(k)$")

# Overlay Binomial distribution
plt.plot(k_values, binomial_p, 'bs-', markersize=5, label=r"Binomial $P_B(k)$")


plt.xlabel("Number of Flares in a Day")
plt.ylabel("Probability")
plt.title("Simulated X-ray Flare Distribution (Per Day)")
plt.legend()
plt.grid()
plt.show()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 20:25:47 2025

@author: kfrench
"""

import numpy as np
import matplotlib.pyplot as plt

# Given probabilities
P_blue = 0.15  #probability of Blue cab
P_green = 0.85  #probability of Green cab

# Range of witness reliability (correctly identifying Blue)
p_values = np.linspace(0, 1, 100)

# Compute probability for each reliability value
changing_blue = (p_values * P_blue) / (p_values * P_blue + (1 - p_values) * P_green)

# Plot the results
plt.figure(figsize=(8, 5))
plt.plot(p_values, changing_blue, label="Probality Correct Witness ID", color="blue")
plt.xlabel("Witness Reliability ")
plt.ylabel("Probability Correct ID")
plt.title("Effect of Witness Reliability on Probability of Correct Color ID")
plt.legend()
plt.grid()
plt.show()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:24:26 2025

@author: kfrench
"""

import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Define the sets' sizes based on probabilities for each scenario
subsets = {
    '100': 0.3,  # Only A
    '010': 0.25, # Only B
    '001': 0.2,  # Only C
    '110': 0.05, # A ∩ B
    '101': 0.04, # A ∩ C
    '011': 0.03, # B ∩ C
    '111': 0.01  # A ∩ B ∩ C
}

# Create Venn diagram
plt.figure(figsize=(6,6))
venn = venn3(subsets=subsets, set_labels=('A', 'B', 'C'))

# Customize the diagram with labels
for subset in venn.set_labels:
    subset.set_fontsize(14)
for subset in venn.subset_labels:
    if subset:
        subset.set_fontsize(12)

# Show plot
plt.title("Venn Diagram Representation of The Law of Addition")
plt.show()

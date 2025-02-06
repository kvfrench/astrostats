#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:37:35 2025

@author: kfrench
"""

import numpy as np

def random_walk_simulation(num_trials=1000):
    # Generate a matrix of shape (num_trials, 3), where each element is -1 or 1
    steps = np.random.choice([-1, 1], size=(num_trials, 3))
    
    final_positions = np.sum(steps, axis=1)
    
    success_count = np.sum(final_positions == 1)
    
  
    probability_estimate = success_count / num_trials
    return probability_estimate


probability = random_walk_simulation()
print(f"Estimated Probability: {probability:.4f}")

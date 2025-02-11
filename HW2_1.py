#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 14:54:02 2025

@author: kfrench
"""

"""
This code explores a permutation problem that I came up with, so there is no citation from a textbook.
The premise of this problem is that you want to paint 5 stripes on a wall in a cafe. 
The five available colors are red, blue, purple, pink, and cyan. 
The owner of the cafe has specified that she doesn't want colors to repeat.
Order matters in this problem, because, for example, if you put red as the first stripe, that is different
than putting red as the second stripe. The colors can be shuffled to sit in each of the five spots.
This coode will calculate how many unique orderings there are. 
It will also calculate some simple probabilites assuming the colors are picked randomly.

"""

import math
import numpy as np
import matplotlib.pyplot as plt

 
#simple application of the permutation formula to determine how many possible orderings there are
n = 5  # Total colors
r = 5  # Colors to arrange
num_permutations = math.factorial(n) // math.factorial(n - r)
print("The total number of permutations of paint stripes:", num_permutations)  

#probability that red will appear in the first column, if randomly choosen
red_1 = math.factorial(4)
prob_red_1 = red_1/num_permutations
print("The probability of randomly getting red as the first stripe:", prob_red_1)

#function to explore probability of picking red first n times
def random_stripe(n_trials):
    colors = np.array(["red","blue","purple","pink","cyan"])
    red_first = 0
    probabilities = []

    for i in range(1, n_trials + 1):
        np.random.shuffle(colors)  # Randomly shuffle colors in-place
        if colors[0] == "red":  # Check if first color is red
            red_first += 1
        
        probabilities.append(red_first / i)  # Running probability

    return probabilities

# Number of trials
n_trials = 1000
probability_convergence = random_stripe(n_trials)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(range(1, n_trials + 1), probability_convergence, label="Simulated Probability")
plt.axhline(y=0.2, color='r', linestyle='--', label="Predicted Probability (0.2)")
plt.xlabel("Number of Trials")
plt.ylabel("Probability")
plt.title(f"Probability of Picking Red First, (n={n_trials})")
plt.grid()
plt.legend()
plt.show()

#It's important to note that the above function and plot can be used for picking any one color in any 
#of the five positions, it's simply for convenience that red and the first column were choosen. 

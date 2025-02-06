#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 12:06:29 2025

@author: kfrench
"""

V = set(range(1, 51)) #Visa card students
M = set(range(26,66)) #Mastercard students
X = set(range(66,101)) #Remaining students

# Question 1: 
#What is the probability that the selected individual has at least one of the two types of cards?

v_or_m = V | M  # Union of V and M

all_students = len(V | M | X)

probability = len(v_or_m) / all_students
print("Probability that the selected student has one of the cards:", probability)

#Question 2:
#What is the probability that the selected individual has neither card type?

probability_neither = len(X) / all_students
print("Probability that the selected student has neither card type:", probability_neither)

#Question 3
#Find the probability that the student has a Visa but not MasterCard.

v_only = V -M

probability_v_only = len(v_only)/ all_students
print("Probability that the selected student has a Visa only:", probability_v_only)

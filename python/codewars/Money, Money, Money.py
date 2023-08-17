# Money, Money, Money
# https://www.codewars.com/kata/563f037412e5ada593000114/python

def calculate_years(P, I, T, D):
    years = 0
    while P < D:
        interest = P * I
        P += interest
        P -= interest * T
        years += 1
    return years



# Best practice
def calculate_years(principal, interest, tax, desired):
    years = 0
    
    while principal < desired:
        principal += (interest * principal) * (1 - tax)
        years += 1
        
    return years



# Clever
from math import ceil, log

def calculate_years(principal, interest, tax, desired):
    if principal >= desired: return 0
    
    return ceil(log(float(desired) / principal, 1 + interest * (1 - tax)))
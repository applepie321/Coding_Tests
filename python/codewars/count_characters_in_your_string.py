# Count characters in your string
# https://www.codewars.com/kata/52efefcbcdf57161d4000091/python



# DESC:
# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.



# Best practice:
from collections import Counter

def count(string):
    return Counter(string)

# Clever
def count(string):
  
    return {i: string.count(i) for i in string}


from collections import Counter as count
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 12:52:20 2016

@author: akshaybudhkar
"""

import matplotlib.pyplot as plt

flex_file = open('flex.txt', 'r')


flex_arr = [int(line) for line in flex_file]

# Bad Flex sensor value
if 1023 in flex_arr:
    flex_arr.remove(1023)

# Do the plotting
plt.plot(flex_arr)
plt.ylabel("Flex sensor analog values")
plt.xlabel("Time")

plt.show()

#close the file
flex_file.close()
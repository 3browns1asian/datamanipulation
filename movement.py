# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 13:28:08 2016

@author: akshaybudhkar
"""

import matplotlib.pyplot as plt

f = open('rotation.txt', 'r')

arr = [[x[1], x[3], x[5]] for x in [line.split() for line in f]]

plt.plot(arr)
plt.legend(["orient_x", "orient_y", "orient_z"])
plt.xlabel("Time")
plt.ylabel("Angular Velocity (in Degrees per Second)")
#plt.ylim([-2, 15])
#plt.xlim([0, 22])
plt.show()

f.close()
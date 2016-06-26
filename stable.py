# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 13:08:01 2016

@author: akshaybudhkar
"""

import matplotlib.pyplot as plt

stable_file = open('stable_acceleration.txt', 'r')

alternate_counter = 0
gyro_vals = []
accl_vals = []

for line in stable_file:
    val = line.split()
    
    if alternate_counter % 2 == 0:
        accl_vals.append([val[1], val[3], val[5]])
    else:
        gyro_vals.append([val[1], val[3], val[5]])
    
    alternate_counter += 1
    

plt.plot(gyro_vals)
plt.legend(["orient_x", "orient_y", "orient_z"])
plt.xlabel("Time")
plt.ylabel("Angular Velocity (in Degrees per Second)")
plt.ylim([-6, 4])
plt.xlim([0, 20])
plt.show()
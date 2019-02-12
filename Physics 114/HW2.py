# Written by - Marchello Caruso
# 2/18/2019
# Forward model of a photometer system for different integrated times
# V1.0.0

# -----------------------------------------------------------------------------
# Propeties needed and known bugs

# 1 - Need a way to find the time associated with a specified data point
#        - possible idea, another for loop in function?
# 2 - Plot Predicted electrons with respect to time in seconds

# ------------------------------------------------------------------------------
# Importing packages

import math
import matplotlib as plt
import numpy as np

# ------------------------------------------------------------------------------
# defining function for the forwardmodel equation

# This function is in the form of a python generator, which doesn't return
# a list of values but returns the computed values one after the other
#             N = (A/4*pi*z^2)(nS)(Eta)(Ta)(deltaT)+(nb)(deltaT)
# nS     - Photons expected from source
# nb     - Photons expected from background
# Eta    - Efficiency of system
# Ta     - Atmospheric Transmission
# deltaT - Time difference in seconds
# z      - Distance between source and reciver in meters


def forwardmodel(diam, z, nS, Eta, Ta, nB, T1, T2):
    for T1 in range(T2 + 1):
        A = 3.14 * ((diam / 2) ** 2)
        deltaT = T1
        N = ((A * nS * Eta * Ta * deltaT) / ((4 * math.pi) * z ** 2)) + (nB * deltaT)
        print(T1)
        T1 = deltaT + 1
        yield(N)


# Calling function and storing data
# PredElec = forwardmodel(.2032, 100, 1000, 0.0855, .9, 1, .01, 100)
for val in forwardmodel(.2032, 100, 1000, 0.0855, .9, 1, 0, 100):
    PredElec = []
    PredElec = PredElec.append(val)

# ------------------------------------------------------------------------------

# plotting the forward model function over a time interval
plt.figure(num="Forwardmodel")

# Formatting
plt.ylabel("Number of Photons Detected")
plt.xlabel("Time [s]")
plt.ylim(-10, 300)
plt.xlim(0, 110)
plt.xticks(np.linspace(0, 110, num=11))
plt.minorticks_on()

# Plotting the Function
plt.plot(T1, PredElec)

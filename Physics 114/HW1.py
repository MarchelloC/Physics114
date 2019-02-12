# Written by - Marchello Caruso
# 2/7/2019
# Reading observation data from text file and plotting the data
# V1.0.0
# -----------------------------------------------------------------------------

# Importing python modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# -----------------------------------------------------------------------------
# Reading data file and placing it into a Data Frame structure from pandas
# Allows for easy manipulation and extraction of data by columns or skip rows
# Pandas also includes statistical analysis of data.

datafile = "C:/Users/Desktop/Desktop/Physics 114/HW_Data/HW1/PHYS114_set1.txt"
df = pd.read_csv(datafile,
                 names=["Year", "Obs"],
                 skiprows=5,
                 index_col=None,)

# Separates columns within the Data Frame for use during plotting

years = df.Year
obs = df.Obs

# -----------------------------------------------------------------------------
# Now we use matplotlib to plot, same procedure as MatLab coding with slight
# variation on syntax.

# Creating a new figure and assigning properties.

# Creates a general figure to work within.
plt.figure(num='Data')

# Formatting x and y axis to specified formatting.
plt.ylabel('Observation', fontsize=12)
plt.xlabel('Year', fontsize=12)
plt.xlim(1880, 2010)
plt.ylim(-1.3, 1.3)
plt.xticks(np.linspace(1880, 2010, num=14))   # manually set x axis scaling
plt.minorticks_on()
plt.tick_params(axis='both', which='both', direction='in', length=3, labelsize=12)
plt.grid()

# Plotting the data into the formatted figure
plt.plot(years, obs, color='grey')
plt.plot(years, obs, 'o', color='black', markersize=2)
plt.show()                                    # opening the figure created

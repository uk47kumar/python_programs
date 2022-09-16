import numpy as np
from scipy import stats

dataset = [1, 1, 2, 3, 4, 6, 7, 5]

# mean value
mean = np.mean(dataset)

# median value
median = np.median(dataset)

# mode value
mode = stats.mode(dataset)

# standard deviation value
standard_Deviation = np.std(dataset)

print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)
print("Standard_Deviation: ", standard_Deviation)

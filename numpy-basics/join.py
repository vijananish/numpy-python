"""
This is about join in numpy
"""
import numpy as np

data1 = np.array([1, 2, 3])
data2 = np.array([4, 5, 6])
# Concatenating
print("________________")
print("Concatenating")
print("________________")
print(np.concatenate((data1, data2)))

# Stacking
print("________________")
print("Stacking")
print("________________")
print(np.stack((data1, data2), axis=0))
print(np.stack((data1, data2), axis=1))

# Horizontal Stack
print("________________")
print("Horizontal Stack")
print("________________")
print(np.hstack((data1, data2)))

# Vertical Stack
print("________________")
print("Vertical Stack")
print("________________")
print(np.vstack((data1, data2)))

# Depth Stack
print("________________")
print("Depth Stack")
print("________________")
print(np.dstack((data1, data2)))

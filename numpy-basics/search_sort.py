"""
This is about searching, sorting and filter in numpy
"""
import numpy as np
data = np.array([2, 1, 5, 3])
print(data)

print("________________")
print("Search")
print("________________")
print(np.where(data == 1))
print("________________")
print("Search Sorted")
print("________________")
print(np.searchsorted(data, 1))
print("________________")
print("Sort")
print("________________")
print(np.sort(data))
print("________________")
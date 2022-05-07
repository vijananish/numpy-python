"""
This about split in numpy
"""
import numpy as np
# 1-D
print("---------------------")
print("1-D split")
print("---------------------")
data_1d = np.array([1, 2, 3, 4, 5])
print(np.array_split(data_1d, 3))

# 2-D
print("---------------------")
print("2-D split")
print("---------------------")
data_np_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]])
print(np.array_split(data_np_2d, 2))
print(np.array_split(data_np_2d, 2, axis=1))

# Horizontal Split
print("---------------------")
print("Horizontal split")
print("---------------------")
print(np.hsplit(data_np_2d, 5))

# Vertical Split
print("---------------------")
print("Vertical split")
print("---------------------")
print(np.vsplit(data_np_2d, 2))

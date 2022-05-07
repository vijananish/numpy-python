"""
Iteration in numpy
"""
import numpy as np
print("________________")
print("Simple iteration")
print("________________")
data = np.array([[1, 2], [5, 6]])

# Simple Iteration
for i in data:
    for j in i:
        print(j)

# Using iter
print("________________")
print("using nditer")
print("________________")
for i in np.nditer(data):
    print(i)

# Using ndenumerate
print("________________")
print("using ndenumerate")
print("________________")
for pos, value in np.ndenumerate(data):
    print(pos, value)

"""
This file contains solution of 51-60 questions
"""
import numpy as np
from io import StringIO

# 51. Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆)
print("-----------------------------------------------------------")
print("51. Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆)")
data = np.ones((3, 3), [('position', [('x', float), ('y', float)]), ('color', [('r', np.compat.unicode),
                                                                               ('g', np.compat.unicode),
                                                                               ('b', np.compat.unicode)])])
print(data)

# 52. Consider a random vector with shape (100,2) representing coordinates, find point by point distances (★★☆)
print("-----------------------------------------------------------")
print("52. Consider a random vector with shape (100,2) representing coordinates, find point by point distances (★★☆)")
x = np.random.random((100, 2))
y = np.random.random((100, 2))
print(abs(x-y))

# 53. How to convert a float (32 bits) array into an integer (32 bits) in place?
print("-----------------------------------------------------------")
print("53. How to convert a float (32 bits) array into an integer (32 bits) in place?")
data = np.array([1, 2, 3, 4], dtype="float32").astype("int32")
print(data)

# 54. How to read the following file? (★★☆)
"""
1, 2, 3, 4, 5
6,  ,  , 7, 8
 ,  , 9,10,11
"""
print("-----------------------------------------------------------")
print("54. How to read the following file? (★★☆)")
text = StringIO("""
1, 2, 3, 4, 5
6,  ,  , 7, 8
 ,  , 9,10,11
""")
data = np.genfromtxt(text, delimiter=",", dtype="int16")
print(data)

# 55. What is the equivalent of enumerate for numpy arrays? (★★☆)
print("-----------------------------------------------------------")
print("55. What is the equivalent of enumerate for numpy arrays? (★★☆)")
data = np.random.randint(1, 10, (2, 2))
for index, value in np.ndenumerate(data):
    print(index, value)

# 56. Generate a generic 2D Gaussian-like array (★★☆)
print("-----------------------------------------------------------")
print("56. Generate a generic 2D Gaussian-like array (★★☆)")
mu = 0
sigma = 1
x = np.array([1, 2, 3])
print(np.exp((-1/2)*(((x-mu)/sigma)**2)))

# 57. How to randomly place p elements in a 2D array? (★★☆)
print("-----------------------------------------------------------")
print("57. How to randomly place p elements in a 2D array? (★★☆)")
data = np.ones((3, 3), dtype="int8")
np.put(data, np.random.choice(range(1, 8), 3, replace=False), 2)
print(data)

# 58. Subtract the mean of each row of a matrix (★★☆)
print("-----------------------------------------------------------")
print("58. Subtract the mean of each row of a matrix (★★☆)")
x = np.array([[1, 2, 3], [4, 5, 6]])
print(x-np.mean(x, axis=1, keepdims=True))

# 59. How to sort an array by the nth column? (★★☆)
print("-----------------------------------------------------------")
print("59. How to sort an array by the nth column? (★★☆)")
data = np.random.random((3, 3))
print(data[data[:, 2].argsort(), :])

# 60. How to tell if a given 2D array has null columns? (★★☆)
print("-----------------------------------------------------------")
print("60. How to tell if a given 2D array has null columns? (★★☆)")
data = np.random.randint(0,3,(3,10)).astype("float")
data[0, 0] = np.nan
if np.any(np.isnan(data).any(axis=0)):
    print("nan value present")
else:
    print("nan not present")
print("-----------------------------------------------------------")

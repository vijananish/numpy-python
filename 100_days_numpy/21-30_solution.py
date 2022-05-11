"""
This file contains solution of 21-30 questions
"""
import numpy as np

# 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)
print("-----------------------------------------------------------")
print("21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)")
print(np.tile(np.array([[0, 1], [1, 0]]), (4, 4)))

# 22. Normalize a 5x5 random matrix (★☆☆)
print("-----------------------------------------------------------")
print("22. Normalize a 5x5 random matrix (★☆☆)")
data = np.random.random((5, 5))
print((data-np.mean(data))/(np.std(data)))

# 23. Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)
print("-----------------------------------------------------------")
print("23. Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)")
rgba = np.dtype([("r", np.ubyte), ("g", np.ubyte), ("b", np.ubyte), ("a", np.ubyte)])

# 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
print("-----------------------------------------------------------")
print("24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)")
print(np.dot(np.random.random((5, 3)), np.random.random((3, 2))))
# 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)
print("-----------------------------------------------------------")
print("25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)")
data = np.random.randint(1, 13, 10, dtype="int8")
data[np.where((data > 3) & (data < 8))] *= -1
print(data)

# 26. What is the output of the following script? (★☆☆)
"""
print(sum(range(5),-1))
"""
print("-----------------------------------------------------------")
print("26. What is the output of the following script? (★☆☆)")
print(np.sum(range(5), -1))

# 27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)
"""
Z**Z
Z <- Z
1j*Z
Z/1/1
"""
print("-----------------------------------------------------------")
print("27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)")
Z = np.ones((5,3))
print(Z)
print(Z**Z)
print(Z < -Z)
print(1j*Z)
print(Z/1/1)

# 28. What are the result of the following expressions? (★☆☆)
"""
np.array(0) / np.array(0)
np.array(0) // np.array(0)
np.array([np.nan]).astype(int).astype(float)
"""
print("-----------------------------------------------------------")
print("28. What are the result of the following expressions? (★☆☆)")
print(np.array(0) / np.array(0))
print(np.array(0) // np.array(0))
print(np.array([np.nan]).astype(int).astype(float))

# 29. How to round away from zero a float array ? (★☆☆)
print("-----------------------------------------------------------")
print("29. How to round away from zero a float array ? (★☆☆)")
data = np.round([11.2, 13.6, 14.09])
print(data)

# 30. How to find common values between two arrays? (★☆☆)
print("-----------------------------------------------------------")
print("30. How to find common values between two arrays? (★☆☆)")
data1 = np.random.randint(0, 10, 10)
data2 = np.random.randint(0, 10, 10)
print(np.intersect1d(data1, data2))
print("-----------------------------------------------------------")

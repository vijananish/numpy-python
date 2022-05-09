"""
This file contains solution of 11-20 questions
"""
import numpy as np

# 11. Create a 3x3 identity matrix (★☆☆)
print("-----------------------------------------------------------")
print("11. Create a 3x3 identity matrix (★☆☆)")
print(np.identity(3, dtype='int8'))

# 12. Create a 3x3x3 array with random values (★☆☆)
print("-----------------------------------------------------------")
print("12. Create a 3x3x3 array with random values (★☆☆)")
print(np.random.randint(1, 30, (3, 3, 3), dtype='int16'))

# 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
print("-----------------------------------------------------------")
print("13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)")
data = np.random.randint(1, 150, (10, 10), dtype="int16")
print("min of numpy data", np.min(data))
print("max of numpy data", np.max(data))

# 14. Create a random vector of size 30 and find the mean value (★☆☆)
print("-----------------------------------------------------------")
print("14. Create a random vector of size 30 and find the mean value (★☆☆)")
data = np.random.randint(1, 150, 10, dtype="int16")
print("mean of data", data.mean())

# 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)
print("-----------------------------------------------------------")
print("15. Create a 2d array with 1 on the border and 0 inside (★☆☆)")
data = np.ones((3, 3), dtype="int8")
data[1:-1, 1:-1] = 0
print(data)

# 16. How to add a border (filled with 0's) around an existing array? (★☆☆)
print("-----------------------------------------------------------")
print("16. How to add a border (filled with 0's) around an existing array? (★☆☆)")
data = np.array([[1, 2, 3, 4]])
print(np.pad(data, 1, mode="constant", constant_values=0))

# 17. What is the result of the following expression? (★☆☆)
"""
0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
np.nan in set([np.nan])
0.3 == 3 * 0.1
"""
print("-----------------------------------------------------------")
print("17. What is the result of the following expression? (★☆☆)")
print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)

# 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
print("-----------------------------------------------------------")
print("18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)")
print(np.diag(np.arange(1, 5), k=-1))

# 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
print("-----------------------------------------------------------")
print("19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)")
data = np.zeros((8, 8))
data[::2, ::2] = 1
data[1::2, 1::2] = 1
print(data)

# 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element? (★☆☆)
print("-----------------------------------------------------------")
print("20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element? (★☆☆)")
data = np.random.randint(1, 1000, (6, 7, 8))
print(data.flatten()[100])
print("-----------------------------------------------------------")

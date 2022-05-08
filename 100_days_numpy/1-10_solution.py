"""
This file contains solution of 1-10 questions
"""

# 1. Import the numpy package under the name (★☆☆)
import numpy as np

# 2. Print the numpy version and the configuration (★☆☆)
print("-----------------------------------------------------------")
print("2. Print the numpy version and the configuration (★☆☆)")
print(np.__version__)

# 3. Create a null vector of size 10 (★☆☆)
print("-----------------------------------------------------------")
print("3. Create a null vector of size 10 (★☆☆)")
print(np.zeros(10, dtype='int8'))

# 4. How to find the memory size of any array (★☆☆)
print("-----------------------------------------------------------")
print("4. How to find the memory size of any array (★☆☆)")
data = np.zeros(10)
print(data.size*data.itemsize)

# 5. How to get the documentation of the numpy add function from the command line? (★☆☆)
print("-----------------------------------------------------------")
print("5. How to get the documentation of the numpy add function from the command line? (★☆☆)")
print("python -c 'import numpy; numpy.info(numpy.add)'")

# 6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
print("-----------------------------------------------------------")
print("6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)")
data = np.zeros(10)
data[4] = 1
print(data)

# 7. Create a vector with values ranging from 10 to 49 (★☆☆)
print("-----------------------------------------------------------")
print("7. Create a vector with values ranging from 10 to 49 (★☆☆)")
print(np.arange(10, 50))

# 8. Reverse a vector (first element becomes last) (★☆☆)
print("-----------------------------------------------------------")
print("8. Reverse a vector (first element becomes last) (★☆☆)")
data = np.array([1, 2, 3, 4])
print(data[::-1])

# 9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
print("-----------------------------------------------------------")
print("9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)")
data = np.arange(0, 9).reshape((3, 3))
print(data)

# 10. Find indices of non-zero elements from [1,2,0,0,4,0]
print("-----------------------------------------------------------")
print("10. Find indices of non-zero elements from [1,2,0,0,4,0]")
data = np.array([1, 2, 0, 0, 4, 0])
print(np.nonzero(data))
print("-----------------------------------------------------------")

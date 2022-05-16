"""
This file contains solution of 21-30 questions
"""
import numpy as np

# 41. How to sum a small array faster than np.sum? (★★☆)
print("-----------------------------------------------------------")
print("41. How to sum a small array faster than np.sum? (★★☆)")
data = np.arange(1, 10)
print(np.add.reduce(data))

# 42. Consider two random array A and B, check if they are equal (★★☆)
print("-----------------------------------------------------------")
print("42. Consider two random array A and B, check if they are equal (★★☆)")
data1 = np.arange(1, 10)
data2 = np.arange(1, 10)
print(np.array_equal(data1, data2))

# 43. Make an array immutable (read-only) (★★☆)
print("-----------------------------------------------------------")
print("43. Make an array immutable (read-only) (★★☆)")
# data = np.arange(1, 10)
# data.flags.writeable = False
# data[1] = 3

# 44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)
print("-----------------------------------------------------------")
print("44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)")
data = np.random.random((10, 2))
print(np.complex128(data))

# 45. Create random vector of size 10 and replace the maximum value by 0 (★★☆)
print("-----------------------------------------------------------")
print("45. Create random vector of size 10 and replace the maximum value by 0 (★★☆)")
data = np.random.randint(1, 13, 10, dtype="int8")
data[np.where(np.max(data))] = 0
print(data)

# 46. Create a structured array with `x` and `y` coordinates covering the [0,1]x[0,1] area (★★☆)
print("-----------------------------------------------------------")
print("46. Create a structured array with `x` and `y` coordinates covering the [0,1]x[0,1] area (★★☆)")
print(np.meshgrid(np.linspace(0, 1, 5), np.linspace(0, 1, 5)))

# 47. Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj)) (★★☆)
print("-----------------------------------------------------------")
print("47. Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj)) (★★☆)")
x = np.random.random((1, 10))
y = np.random.random((1, 10))
C = np.divide(1, np.subtract(x, y))

# 48. Print the minimum and maximum representable value for each numpy scalar type (★★☆)
print("-----------------------------------------------------------")
print("48. Print the minimum and maximum representable value for each numpy scalar type (★★☆)")
for dtype in [np.int8, np.int32, np.int64]:
   print(np.iinfo(dtype).min)
   print(np.iinfo(dtype).max)
for dtype in [np.float32, np.float64]:
   print(np.finfo(dtype).min)
   print(np.finfo(dtype).max)

# 49. How to print all the values of an array? (★★☆)
print("-----------------------------------------------------------")
print("49. How to print all the values of an array? (★★☆)")
data = np.random.random((10, 10))
print(data)

# 50. How to find the closest value (to a given scalar) in a vector? (★★☆)
print("-----------------------------------------------------------")
print("50. How to find the closest value (to a given scalar) in a vector? (★★☆)")
data1 = np.arange(100)
data2 = np.random.uniform(0, 100)
index = (np.abs(data1-data2)).argmin()
print(data1[index])
print("-----------------------------------------------------------")

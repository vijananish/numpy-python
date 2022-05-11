"""
This file contains solution of 31-40 questions
"""
import numpy as np

# 31. How to ignore all numpy warnings (not recommended)?
print("-----------------------------------------------------------")
print("31. How to ignore all numpy warnings (not recommended)?")
defaults = np.seterr(all="ignore")
Z = np.ones(1) / 0
print(Z)

# 32. Is the following expressions true? (★☆☆)
"""
np.sqrt(-1) == np.emath.sqrt(-1)
"""
print("-----------------------------------------------------------")
print("32. Is the following expressions true? (★☆☆)")
print(np.sqrt(-1) == np.emath.sqrt(-1))

# 33. How to get the dates of yesterday, today and tomorrow? (★☆☆)
print("-----------------------------------------------------------")
print("33. How to get the dates of yesterday, today and tomorrow? (★☆☆)")
today = np.datetime64('today', 'D')
print("Today: ", today)
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
print("Yesterday: ", yesterday)
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("Tomorrow: ", tomorrow)

# 34. How to get all the dates corresponding to the month of July 2016? (★★☆)
print("-----------------------------------------------------------")
print("34. How to get all the dates corresponding to the month of July 2016? (★★☆)")
print(np.arange("2016-07", "2016-08", dtype="datetime64[D]"))

# 35. How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)
print("-----------------------------------------------------------")
print("35. How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)")
A = np.ones(3)*4
B = np.ones(3)*2
np.add(A, B, out=B)
np.negative(A, out=A)
np.divide(A, 2, out=A)
np.multiply(B, A, out=B)
print(B)

# 36. Extract the integer part of a random array of positive numbers using 4 different methods (★★☆)
print("-----------------------------------------------------------")
print("36. Extract the integer part of a random array of positive numbers using 4 different methods (★★☆)")

Z = np.random.uniform(0, 10, 10)
print(Z - Z % 1)
print(Z // 1)
print(np.floor(Z))
print(Z.astype(int))
print(np.trunc(Z))

# 37. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)
print("-----------------------------------------------------------")
print("37. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)")
Z = np.zeros((5, 5)) + np.arange(0, 5)
print(Z)

# 38. Consider a generator function that generates 10 integers and use it to build an array (★☆☆)
print("-----------------------------------------------------------")
print("38. Consider a generator function that generates 10 integers and use it to build an array (★☆☆)")


def generator():
    for i in range(10):
        yield i


Z = np.fromiter(generator(), dtype="int16")
print(Z)

# 39. Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)
print("-----------------------------------------------------------")
print("39. Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)")
data = np.linspace(0, 1, 11, endpoint=False)[1:]
print(data)

# 40. Create a random vector of size 10 and sort it (★★☆)
print("-----------------------------------------------------------")
print("40. Create a random vector of size 10 and sort it (★★☆)")
print(np.sort(np.random.random(10)))
print("-----------------------------------------------------------")

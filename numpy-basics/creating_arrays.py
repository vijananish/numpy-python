"""
This is about basic array creation in numpy
"""
import numpy as np
"""
1. Python Structure (List, Tuple)
2. Numpy array creation object (ones, zeros, linspace, arange)
3. Reading from disk
4. Array from bytes
5. Special Library Function (random)
"""
# ----------------
# Python Structure
# ----------------
print("-----------------------------")
print("Python Structure")
print("-----------------------------")
# 1-D
data_np_1d = np.array([1, 2, 3, 4, 5])
print("1-D Python Structure: ")
print(data_np_1d)

# 2-D
data_np_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]])
print("2-D Python Structure: ")
print(data_np_2d)

# 3-D
data_np_3d = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]],
                       [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]])
print("3-D Python Structure: ")
print(data_np_3d)

# ---------------------------
# Numpy Array creation object
# ---------------------------
print("-----------------------------")
print("Numpy Array creation object")
print("-----------------------------")
print(np.ones([3, 3]))
print(np.zeros([3, 3]))
print(np.linspace(1, 10, 10))
print(np.arange(10))

# ---------------------
# Reading from the disk
# ---------------------
print("-----------------------------")
print("Reading from the disk")
print("-----------------------------")
filename = "numpy_disk.dat"
disk_save = np.memmap(filename, dtype="int64", mode="w+", shape=(3, 3))
disk_save[0] = [1, 2, 3]
disk_save.flush()
print(np.memmap(filename, dtype="int64", mode="r", shape=(3, 3)))

# ----------------
# Array from Bytes
# ----------------
print("-----------------------------")
print("Array from Bytes")
print("-----------------------------")
data_np = np.array([1, 2, 3, 4, 5])
numpy_bytes = data_np.tobytes()
deserialized_bytes = np.frombuffer(numpy_bytes, dtype="int32")
print(deserialized_bytes)

# ------------------------
# Special Library Function
# ------------------------
print("-----------------------------")
print("Special Library Function")
print("-----------------------------")
print(np.random.rand(10))
print("-----------------------------")

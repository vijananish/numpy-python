"""
This is about indexing and slicing in numpy arrays.
"""
import numpy as np
# 1-D
data_np_1d = np.array([1, 2, 3, 4, 5])
print("indexing 1-D:", data_np_1d[1])
print("slicing 1-D:", data_np_1d[2:])
print("dtype 1-D:", data_np_1d.dtype)

# 2-D
data_np_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]])
print("indexing 2-D:", data_np_2d[1, 3])
print("slicing 2-D:", data_np_2d[:, 3])
print("dtype 2-D:", data_np_2d.dtype)

# 3-D
data_np_3d = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]],
                       [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]])
print("indexing 3-D:", data_np_3d[1, 1, 2])
print("slicing 3-D:", data_np_3d[:, 1, 3])
print("dtype 3-D:", data_np_3d.dtype)

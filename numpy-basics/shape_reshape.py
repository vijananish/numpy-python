"""
This is about shape of the array and reshaping the array
"""
import numpy as np
# 1-D
data_np_1d = np.array([1, 2, 3, 4, 5])
print("1-D Python Structure: ", data_np_1d.shape)
data_np_1d_reshape = data_np_1d.reshape((5, 1))
print("Data Reshaped")
print(data_np_1d_reshape)

# 2-D
data_np_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]])
print("2-D Python Structure: ", data_np_2d.shape)
data_np_2d_reshape = data_np_2d.reshape((5, 2))
print("Data Reshaped")
print(data_np_2d_reshape)

# 3-D
data_np_3d = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]],
                       [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]])
print("3-D Python Structure: ", data_np_3d.shape)
data_np_3d_reshape = data_np_3d.reshape((4, 5))
print("Data Reshaped")
print(data_np_3d_reshape)

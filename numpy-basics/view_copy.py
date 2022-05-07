"""
This is about view and copy in numpy
"""
import numpy as np
# View
print("-------------")
print("view")
print("-------------")
data = np.array([1, 2, 3, 4])
view_data = data.view()
data[0] = 3
view_data[2] = 100
print(data)
print(view_data)

# Copy
print("-------------")
print("copy")
print("-------------")
copy_data = data.copy()
data[0] = 10
copy_data[1] = 45
print(data)
print(copy_data)

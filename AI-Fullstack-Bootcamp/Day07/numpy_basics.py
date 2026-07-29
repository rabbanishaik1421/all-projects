import numpy as np

# print(np.__version__)

# 1. One-Dimensional Array (1D)
a = np.array([1, 2, 3, 4])
# print(a)

# 2. Two-Dimensional Array (2D)
a = np.array([[1, 2], [3, 4]])
# print(a)

# 3. Three-Dimensional Array (3D)
a = np.array([[1,2], [3,4], [5,6]])
print(a)

# 4. Check Number of Dimensions
a = np.array([[1, 2], [3, 4]])
# print(a.ndim)

# 5. Shape means rows and columns.
a = np.array([[1,2,3], [4,5,6]]) 
# print(a.shape)

# 6. Number of elements.
a = np.array([[1,2,3], [4,5,6]]) 
# print(a.size)

# 7. Data Type
a = np.array([[10, 20, 30]])
# print(a.dtype)

# 8. Item Size
a = np.array([[1,2,3], [4,5,6]])
# print(a.itemsize)

# 9.Total Memory Used
a = np.array([1, 2, 3])
# print(a.nbytes)

# 10. Create Array Using Range
a = np.arange(1, 11)
# print(a)

# 11. arange with step
a = np.arange(1, 11, 2)
# print(a)

# 12. linspace()
a = np.arange(1, 10, 5)
# print(a)

# 13. zeros()
a = np.zeros((3, 4))
# print(a)

# 14. ones()
a = np.ones((2, 3))
# print(a)

# 15. full() //Fill with same value. 
a = np.full((2,2), 7)
# print(a)

# 16. eye() //Identity Matrix
a = np.eye(3)
# print(a)

# 17.random.rand() //Random numbers between 0 and 1
a = np.random.rand(3)
# print(a)

# 18.random.randint()
a = np.random.randint(1, 100, 3)
# print(a)

# 19.Slicing
a = np.array([10,20,30,40,50])
# print(a[1:4])

# 20. Reshape
# Convert array dimensions.
a = np.arange(1,13)

# print(a.reshape(3,4))

# 21.Convert multi-dimensional array into 1D.

import numpy as np

arr = np.array([[1, 2, 3]])
print(arr +10) 


matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector =np.array([1, 0, 1])
print(matrix + vector)  # Broadcasting the vector across the rows of the matrix
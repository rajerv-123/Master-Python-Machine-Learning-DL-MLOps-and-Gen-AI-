import numpy as np

# arr=np.array([[1,2,3],[4,5,6]])
# print("sum",np.sum(arr))
# print("Max",np.max(arr))
# print("Min",np.min(arr))
# print("Mean",np.mean(arr))
# print("Median",np.median(arr))
# print("Standard Deviation",np.std(arr))
# print("Variance",np.var(arr))
# print("Shape",arr.shape)


# arr =np.array([[1,2,3],[4,5,6]])

# even=arr[arr%2==0]
# print("Even numbers in the array:", even)

# arr[arr>2]=0
# print("Array after replacing elements greater than 2 with 0:\n", arr)


np.random.seed()

random_array = np.random.randint(1, 101, size=(2, 2))
print("Random Array:\n", random_array)

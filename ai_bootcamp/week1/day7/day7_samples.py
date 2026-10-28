# [expression for item in iterable if condition]

# create a list of squares for even numbers from 0 to 9.
from functools import reduce


square = [x**2 for x in range(1000)]
# print(square)

# filter even number
evens = [x for x in range(100) if x % 2 == 0]
# print(evens)

#lambda function
# lambda function is a small anonymous function.

# add = lambda x, y: x + y
# print(add(5, 3))  # Output: 8

# map filter reduce
numbers = [1, 2, 3, 4, 5]
squared_number = list(map(lambda x: x**2, numbers))
# print(squared_number)  # Output: [1, 4, 9, 16, 25]

evens = filter(lambda x: x % 2 == 0, numbers)
# print(list(evens))  # Output: [2, 4]

product = reduce(lambda x,y:x*y,numbers);
print(product)  # Output: 120



# touples are immutable, meaning they cannot be changed after creation
# colors = ("red", "green", "blue", "yellow", "purple")
# single_item=("orange",)  # Note the comma to make it a tuple

# print(colors[0])
# print(colors[-1])

# dictionaries are mutable, meaning they can be changed after creation
# student = {"name": "John", "age": 20, "major": "Computer Science"}
# print(student["name"])  # Output: John
# print(student["age"])   # Output: 20
# print(student["major"]) # Output: Computer Science
# student["age"]=55
# print(student["age"])   # Output: 55-is-updates
# print(student)

# del student["major"]  # Remove the "major" key-value pair
# print(student)


student = {"name": "John", "age": 20, "major": "Computer Science"}

for key, value in student.items():
    print(f"{key}: {value}")
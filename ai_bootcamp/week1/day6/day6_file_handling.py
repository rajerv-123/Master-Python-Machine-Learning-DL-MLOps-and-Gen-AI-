# with open("sample.txt", "r") as file:
#     content = file.read()
#     print(content)
#     file.close()  # Close the file after reading


try:
    with open("sample.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")
# num = int(input("Enter a number: "))

# if num > 0:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print(num, "is not a prime number.")
#             break
#     else:
#         print(num, "is a prime number.")
# else:
#     print(num, "is not a prime number.")

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b    

def divide(a,b):
    return a / b

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        if num2 != 0:
            print(num1, "/", num2, "=", divide(num1, num2))
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid input")
        
        
calculator()


        
    

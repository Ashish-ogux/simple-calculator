# to create a simple calulator
# 1. function for operations
# 2. take input from user
# 3. print the result
 
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def avg(x,y):
    return (x+y)/2

print("Select operation:\n1.Add\n" \
"2.Subtract\n" \
"3.Multiply\n" \
"4.Divide\n" \
"5.Average\n")
choice = input("Enter choice(1/2/3/4/5):")
 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
elif choice == '5':
    print("Average of", num1, "and", num2, "is", avg(num1, num2))
else:
    print("Invalid input")

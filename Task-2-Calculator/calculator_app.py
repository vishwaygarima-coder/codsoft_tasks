print("==== SIMPLE CALCULATOR ====")

#Take two numbers from the user
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

#Display operations
print("\nChoose an operation:")
print("+ Addition")
print("- Subtaction")
print("* Multiplication")
print("/ Division")

#Take operation choice
choice = input("Enter your choice:")

#Perform calculation
if choice == "+":
    result = num1 + num2
    print("Result:", result)
    
elif choice == "-":
    result = num1 - num2
    print("Result:", result)
    
elif choice == "*":
    result = num1 * num2
    print("Result:", result)
    
elif choice == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error! Division by zero is not allowed.")
        
else:
    print("Invalid operation")                      

def perform_operation(num1,num2,operation):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()
    if operation == "add":
        return num1 + num2
    elif operation== "subtract":
         return num1 - num2
    elif operation == "mutliply":
         return num1 *  num2
    elif operation == "divide":
        if num2 ==0:
                return "Division by zero, impossible"
        return num1 / num2
      
    else:
         return "Invalid operation, please try again" 

# it is imported to be used in main.py
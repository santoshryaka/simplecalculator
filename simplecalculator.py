#It's simple calculator 
print("_________Simple Calculator_________")

#Enter the two numbers
a = float(input("Enter first number:"))
b = float(input("Enter second number:"))

#Choose the operator 
print("Choose operation(+, -, *, /):")
op = input("Enter operator:")

#Here the condition will start based on operator
if op == '+':
    print("Result:",a + b)
elif op == '-':
    print("Result:",a - b)
elif op == '*':
    print("Result:",a * b)
elif op == '/':
    if b != 0:
        print("Result:",a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
    
print("__________Thank you_________")

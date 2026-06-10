#simple calculator using python 
print("Simple Calculator")

#Enter the two numbers
a = float(input("Enter first number:"))
b = float(input("Enter second number:"))

#Choose the operator 
print("Choose operation(+, -, *, /) for calculation")
op = input("Enter operator:")

#Here the condition will checks based on operator
if op == '+':
    print("Result:",a + b)
elif op == '-':
    print("Result:",a - b)
elif op == '*':
    print("Result:",a * b)
elif op == '/':
    if b!= 0:
        print("Result:",a / b)
    else:
        print("zero division error")
else:
    print("Invalid operator")
    
print("_______Thank you_______")

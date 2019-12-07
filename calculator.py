x=float(input("x="))
y=float(input("y="))
operation=input("Operation:")

result=None

if operation == "+":
    result= x+y
elif operation == "-":
    result = x-y
elif operation == "*":
    result = x*y
elif operation == "/":
    result = x/y
elif operation == "**":
    result = x**y
else: 
    print ("Unknown operation")
    
if result is not None:
    print ("Result:",result) 
    

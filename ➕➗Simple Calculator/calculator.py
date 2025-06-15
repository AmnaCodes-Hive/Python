num1 = int(input("Enter 1st number here:"))
num2 = int(input("Enter 2nd number here:"))
operator = input("Enter operator (+,-,/,*,**,%,//)")
if operator == "+":
    print(f"This will perform addition operation {num1+num2}")
elif operator == "-":
    print(f"This will perform Substraction operation {num1-num2}")
elif operator == "/":
    if num2 !=0:
        print(f"This will perform Division operation {num1/num2}")
    else:
        print("Error: Division by zero is not allowed.")
elif operator == "*":
    print(f"This will perform Multiplication operation {num1*num2}")
elif operator == "**":
    print(f"This will perform square operation {num1**num2}")
elif operator == "//":
    if num2 != 0:
        print(f"This will perform Floor Division: {num1 // num2}")
    else:
        print("Error: Floor division by zero is not allowed.")
elif operator == "%":
    if num2 != 0:
        print(f"This will perform Modulus: {num1 % num2}")
    else:
        print("Error: Modulus by zero is not allowed.")
else:
    print("Invalid numbers or operator")
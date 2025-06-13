Age = int(input("Enter Your Age Here:"))

if Age <= 0:
    print("Sorry You are Not Born Yet😂🤣")
elif Age <= 12:
    print("You Are a Child")
elif Age <= 19:
    print("You Are a Teenager")
elif Age <= 59:
    print("You Are a Adult")
else:
    print("You Are a Senior Citizen")
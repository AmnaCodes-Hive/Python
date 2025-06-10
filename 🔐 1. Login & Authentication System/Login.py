users = {
    "user1":"pass1",
    "user2":"pass2",
    "user3":"pass3",
    "user4":"pass4"
}
Attempts = 3

while Attempts > 0:
    print("ENTER YOUR VALID USERNAME AND PASSWORD")
    username = input("Enter your username")
    password = input("Enter your password")
    
    if username in users and users[username] == password:
        print("Valid credentials",username,"login attempt sucessfull, Welcome.") 
        break
    else:
        Attempts -=1
        print(f"Failed login attempt {username}, Try Again")
    if Attempts == 0:
        print("You have tried loging in many times, Account Locked")
        break
        
    

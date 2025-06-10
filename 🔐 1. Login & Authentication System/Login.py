#Storing password and username in form of dictonary key value pair
users = {
    "user1":"pass1",
    "user2":"pass2",
    "user3":"pass3",
    "user4":"pass4"
}
#Setting the limit of login attempt to 3 
Attempts = 3

#Using while loop for determining the total attempts 
while Attempts > 0:
    print("ENTER YOUR VALID USERNAME AND PASSWORD")
    username = input("Enter your username")
    password = input("Enter your password")

#checking if the username entered by user and credentials saved are same  
    if username in users and users[username] == password:
        print("Valid credentials",username,"login attempt sucessfull, Welcome.") 
        break
    else:
 
#if the credentials are not same only 2 attempt left 1 is chance is used
        Attempts -=1
        print(f"Failed login attempt {username}, Try Again")

#All the attempts are used no chance is left account is locked now
    if Attempts == 0:
        print("You have tried loging in many times, Account Locked")
        break
        
    

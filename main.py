import CreatePasswords as MyPassword


while 1:
    userPasswordLength = int(input("Enter Length For Your Password: "))
    print(MyPassword.GeneratePassword(userPasswordLength))
    userReply = input("Do You Want More?  y / n : ")
    if userReply == 'y' :
        continue
    elif userReply == 'n':
        break
    

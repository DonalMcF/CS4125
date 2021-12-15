import loadFiles 
def logIn():
    currentUser = ""
    log = False
    loop = True
    i = 0
 
    while loop == True:
        if i < 3:
            usernameInput = input('Enter your username: ')
            passwordInput = input('Enter your password: ')
            for obj in loadFiles.accounts:
                if usernameInput == obj.name and passwordInput == obj.password:
                    print("login success!")
                    currentUser = usernameInput
                    currentPassword = passwordInput
                    log = True
                    loop = False
            if log == False:
                print("login failed, check username and password, you have", 2 - i, "attempts left", sep =' ')
                i += 1
        else:
            loop = False
    return currentUser, passwordInput

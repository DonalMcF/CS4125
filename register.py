import loadFiles
def register():
    loop = True
    check = False
    lineNumber = len(loadFiles.accounts)
    while loop == True:
        check = False
        usernameInput = input('Choose a username\n')
        for obj in loadFiles.accounts:
            if obj.name == usernameInput:
                print("Username has been taken, please select another")
                check = True
        if check == False:
            loop = False
    passwordInput = input('Choose a password\n')
    
    textLine = "\n" + usernameInput + ", " + passwordInput + ", user"
    outF = open('accounts.txt', 'a')
    outF.write(textLine)
    outF.close
    loadFiles.accounts.append(loadFiles.accountsFormat(usernameInput,passwordInput,"user"))
    print("Account has been created")
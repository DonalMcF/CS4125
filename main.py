import loadFiles 
import loadUser
import logIn
import register
import purchaseGame
import rentGame
import addGame

userType = ""
userRental = ""

print("New releases this week")
for obj in loadFiles.gameLibrary:
    if obj.newRelease == "yes":
        print(obj.name)
print("\n")

menu1 = True
while menu1 == True:
    userInput = input("What would you like to do? \n1) Register an account\n2) Log in\n3) Exit\n")
    if userInput == "1":
        register.register()
    elif userInput == "2":
        currentUser, currentPassword = logIn.logIn()
        if currentUser:
            print("Welcome,", currentUser, sep = ' ')
            for obj in loadFiles.accounts:
                if currentUser == obj.name:
                    userType = obj.accountType
                    userRental = loadUser.loadUser(currentUser)
                    menu2 = True 
                    while menu2 == True:
                        if userType == "user":
                            userInput = input("What would you like to do? \n1) Purchase game\n2) Subscribe to membership\n3) Log out\n")
                        elif userType == "member":
                            userInput = input("What would you like to do? \n1) Purchase game\n2) Cancel membership\n3) Rent Game\n4) Return Game\n5) Log out\n")
                        elif userType == "admin":
                            userInput = input("What would you like to do? \n1) Purchase game\n2) Add game\n3) Log out\n")
                  
                        #user commands
                        if userInput == "1":
                            purchaseGame.purchaseMenu(currentUser, userType)
                            loadUser.updateUser(currentUser)
                        elif userInput == "2" and (userType == "user" or userType == "member"):
                            userType = loadFiles.updateMembership(currentUser, userType)
                        elif userInput == "3" and userType == "user":
                            print("Goodbye", currentUser, sep = ' ')
                            menu2 = False
                      
                        #member commands
                        elif userInput == "3" and userType == "member":
                            userRental = rentGame.rentGame(userRental)
                            loadUser.updateUserRent(currentUser, userRental)
                        elif userInput == "4" and userType == "member":
                            userRental = rentGame.returnGame(userRental)
                            loadUser.updateUserRent(currentUser, userRental)
                        elif userInput == "5" and userType == "member":
                            print("Goodbye", currentUser, sep = ' ')
                            menu2 = False
                                    
                        #admin commands
                        elif userInput == "2" and userType == "admin":
                            addGame.addGame()
                        elif userInput == "3" and userType == "admin":
                            print("Goodbye", currentUser, sep = ' ')
                            currentUser = ""
                            currentPassword = ""
                            userType = ""
                            userRental = ""
                            loadUser.userLibrary.clear()
                            menu2 = False
                                    
                        else:
                            print("invalid input, please select the number of the action you wish to take")

    elif userInput == "3":
        menu1 = False
    else:
        print("invalid input, please select the number of the action you wish to take")
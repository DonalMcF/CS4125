import loadFiles 
import loadUser
import logIn
import purchaseGame
import rentGame

userType = ""
userRental = ""

print("New releases this week")
for obj in loadFiles.gameLibrary:
    if obj.newRelease == "yes":
        print(obj.name)
print("\n")

currentUser, currentPassword = logIn.logIn()
if currentUser:
    print("Welcome,", currentUser, sep = ' ')
    for obj in loadFiles.accounts:
        if currentUser == obj.name:
            userType = obj.accountType
            userRental = loadUser.loadUser(currentUser)
            loop = True
            while loop == True:
                if userType == "user":
                    userInput = input("What would you like to do? \n1) Purchase game\n2) Subscribe to membership\n3) Exit\n")
                elif userType == "member":
                    userInput = input("What would you like to do? \n1) Purchase game\n2) Cancel membership\n3) Rent Game\n4) Return Game\n5) Exit\n")
                elif userType == "admin":
                    userInput = input("What would you like to do? \n1) Purchase game\n2) Exit\n")
  
                #user commands
                if userInput == "1":
                    purchaseGame.purchaseMenu(currentUser, userType)
                    loadUser.updateUser(currentUser)
                elif userInput == "2" and (userType == "user" or userType == "member"):
                    userType = loadFiles.updateMembership(currentUser, userType)
                elif userInput == "3" and userType == "user":
                    print("Goodbye", currentUser, sep = ' ')
                    loop = False
      
                #member commands
                elif userInput == "3" and userType == "member":
                    userRental = rentGame.rentGame(userRental)
                    loadUser.updateUserRent(currentUser, userRental)
                elif userInput == "4" and userType == "member":
                    userRental = rentGame.returnGame(userRental)
                    loadUser.updateUserRent(currentUser, userRental)
                elif userInput == "5" and userType == "member":
                    print("Goodbye", currentUser, sep = ' ')
                    loop = False
                    
                #admin commands
                elif userInput == "2" and userType == "admin":
                    print("Goodbye", currentUser, sep = ' ')
                    loop = False
                    
                else:
                    print("invalid input, please select the number of the action you wish to take")
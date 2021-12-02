import loadFiles
import loadUser

def rentGame(userRental):
    if not userRental:
        menu = True
        while menu == True:
            check = False
            for obj in loadFiles.gameLibrary:
                print("Name:", obj.name, sep = ' ')
                print("Genre:", obj.genre, sep = ' ')
                print()
            userInput = input("what game would you like to rent?\n'exit' to cancel\n")
            if userInput == "exit":
                menu = False
            for obj in loadFiles.gameLibrary:
                if userInput == obj.name:
                    check = True 
            if check == True:
                userRental = userInput
                print("You have rented" ,userInput, sep = ' ')
                menu = False
            elif check == False and menu == True:
                print("Not a valid Option") 
        return userRental
    else:
        print("Please return rented game before renting another")
        return userRental

def returnGame(userRental):
    if userRental:
        print("You have returned your rented game")
        userRental = ""
        return userRental
    else:
        print("You do not currently have any games rented")
        return userRental
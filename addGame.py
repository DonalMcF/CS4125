import loadFiles
def addGame():
    loop = True
    loop2 = True
    check = False
    lineNumber = len(loadFiles.gameLibrary)
    check = False
    gameGenre = ""
    gameInput = input('What game is being added\n')
    for obj in loadFiles.gameLibrary:
        if obj.name == gameInput:
            print("Game has already been added")
            check = True
    if check == False:
        while loop == True:
            adminInput = input('What genre is it?\n1)Childrens\n2)Teens\n')
            if adminInput == "1":
                gameGenre = "childrens"
                loop = False
            elif adminInput == "2":
                gameGenre = "teens"
                loop = False
            else:
                print("invalid option")
        while loop2 == True:
            gamePrice = input('What is the games base price\n')
            try:
                check = float(gamePrice)
                loop2 = False
            except:
                print("input must be a number")
        
        textLine = "\n" + gameInput + ", " + gameGenre + ", yes, " + gamePrice
        outF = open('gameLibrary.txt', 'a')
        outF.write(textLine)
        outF.close
        loadFiles.gameLibrary.append(loadFiles.gameLibraryFormat(gameInput,gameGenre,"yes",gamePrice.replace("\n","")))
        print("Game has been created")
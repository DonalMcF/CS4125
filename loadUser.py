userLibrary = []
class userLibraryFormat:
    def __init__(self, name, genre, newRelease, pPrice):
        self.name = name
        self.genre = genre
        self.newRelease = newRelease
        self.pPrice = pPrice

def loadUser(currentUser):
    try:
        filename = currentUser + "Library.txt"
        with open(filename,'r') as f:
            textlines = f.readlines()
    
            for i in textlines:
                line = i.split(", ")
                userLibrary.append(userLibraryFormat(line[0],line[1],line[2],line[3].replace("\n","")))
            f.close()
    except:
        filename = currentUser + "Library.txt"
        outF = open(filename, 'w')
        outF.close()
    
    try:
        filename = currentUser + "Rental.txt"
        with open(filename,'r') as f:
            textlines = f.readlines()
            userRental = textlines[0].replace("\n","")
            return userRental
            f.close() 
    except:
        filename = currentUser + "Rental.txt"
        outF = open(filename, 'w')
        outF.close()
    
def updateUser(currentUser):
    filename = currentUser + "Library.txt"
    outF = open(filename, 'w')
    linenumber = len(userLibrary)
    i = 0
    for obj in userLibrary:
        i = i + 1
        if i == len(userLibrary):
            newline = obj.name + ", " + obj.genre + ", " + obj.newRelease + ", " + obj.pPrice
            outF.write(newline)
        else:
            newline = newline = obj.name + ", " + obj.genre + ", " + obj.newRelease + ", " + obj.pPrice + "\n"
            outF.write(newline)
    outF.close()

def updateUserRent(currentUser, userRental):
    filename = currentUser + "Rental.txt"
    outF = open(filename, 'w')
    outF.write(userRental)
    outF.close()
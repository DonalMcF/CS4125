accounts = []
gameLibrary = []
Observables = []

class Observer:

    def __init__(self, observable):
        observable.subscribe(self)

    def notify(
        self,
        observable,
        *args,
        **kwargs
        ):
        print ('Got', args, kwargs, 'From', observable)
    
        
    
class Observable:

    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for obs in self._observers:
            obs.notify(self, *args, **kwargs)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

class accountsFormat:
    def __init__(self, name, password, accountType):
        self.name = name
        self.password = password
        self.accountType = accountType
        

class gameLibraryFormat:
    def __init__(self, name, genre, newRelease, pPrice):
        self.name = name
        self.genre = genre
        self.newRelease = newRelease
        self.pPrice = pPrice

with open('accounts.txt','r') as f:
    textlines = f.readlines()
    
    for i in textlines:
        line = i.split(", ")
        accounts.append(accountsFormat(line[0],line[1],line[2].replace("\n","")))
    f.close()    

with open('gameLibrary.txt','r') as f:
    textlines = f.readlines()
    
    for i in textlines:
        line = i.split(", ")
        gameLibrary.append(gameLibraryFormat(line[0],line[1],line[2],line[3].replace("\n","")))
    f.close() 
    
def updateMembership(currentUser, userType):
    if userType == "user":
        userType = "member"
        outF = open('accounts.txt', 'w')
        linenumber = len(accounts)
        i = 0
        for obj in accounts:
            i = i + 1
            if currentUser == obj.name and i == len(accounts):
                newline = obj.name + ", " + obj.password + ", member"
                outF.write(newline)
            elif currentUser != obj.name and i == len(accounts):
                newline = obj.name + ", " + obj.password + ", " + obj.accountType
                outF.write(newline)
            elif currentUser == obj.name:
                newline = obj.name + ", " + obj.password + ", member\n"
                outF.write(newline)
            else:
                newline = obj.name + ", " + obj.password + ", " + obj.accountType + "\n"
                outF.write(newline)
        outF.close()
        userType = "member"
        
    elif userType == "member":
        outF = open('accounts.txt', 'w')
        linenumber = len(accounts)
        i = 0
        for obj in accounts:
            i = i + 1
            if currentUser == obj.name and i == len(accounts):
                newline = obj.name + ", " + obj.password + ", user"
                outF.write(newline)
            elif currentUser != obj.name and i == len(accounts):
                newline = obj.name + ", " + obj.password + ", " + obj.accountType
                outF.write(newline)
            elif currentUser == obj.name:
                newline = obj.name + ", " + obj.password + ", user\n"
                outF.write(newline)
            else:
                newline = obj.name + ", " + obj.password + ", " + obj.accountType + "\n"
                outF.write(newline)
        outF.close()
        userType = "user"
    return userType

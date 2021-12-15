accounts = []
game_library = []
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

class accounts_format:
    def __init__(self, name, password, account_type):
        self.name = name
        self.password = password
        self.account_type = account_type
class game_library_format:
    def __init__(self, name, genre, new_release, p_price):
        self.name = name
        self.genre = genre
        self.new_release = new_release
        self.p_price = p_price

with open('accounts.txt','r') as f:
    textlines = f.readlines()
    for i in textlines:
        line = i.split(", ")
        accounts.append(accounts_format(line[0],line[1],line[2].replace("\n","")))
    f.close()

with open('gameLibrary.txt','r') as f:
    textlines = f.readlines()
    for i in textlines:
        line = i.split(", ")
        game_library.append(game_library_format(line[0],line[1],line[2],line[3].replace("\n","")))
    f.close()
def update_membership(current_user, user_type):
    if user_type == "user":
        user_type = "member"
        out_f = open('accounts.txt', 'w')
        i = 0
        for obj in accounts:
            i = i + 1
            if current_user == obj.name and i == len(accounts):
                newline = obj.name + ", " + obj.password + ", member"
                out_f.write(newline)
            elif current_user != obj.name and i == len(accounts):
                newline = obj.name + ", " + obj.password + ", " + obj.accountType
                out_f.write(newline)
            elif current_user == obj.name:
                newline = obj.name + ", " + obj.password + ", member\n"
                out_f.write(newline)
            else:
                newline = obj.name + ", " + obj.password + ", " + obj.accountType + "\n"
                out_f.write(newline)
        out_f.close()
        user_type = "member"
    elif user_type == "member":
        out_f = open('accounts.txt', 'w')
        line_number = len(accounts)
        i = 0
        for obj in accounts:
            i = i + 1
            if current_user == obj.name and i == len(accounts):
                newline = obj.name + ", " + obj.password + ", user"
                out_f.write(newline)
            elif current_user != obj.name and i == len(accounts):
                newline = obj.name + ", " + obj.password + ", " + obj.accountType
                out_f.write(newline)
            elif current_user == obj.name:
                newline = obj.name + ", " + obj.password + ", user\n"
                out_f.write(newline)
            else:
                newline = obj.name + ", " + obj.password + ", " + obj.accountType + "\n"
                out_f.write(newline)
        out_f.close()
        user_type = "user"
    return user_type

import load_files
def log_in():
    current_user = ""
    log = False
    loop = True
    i = 0
    while loop is True:
        if i < 3:
            username_input = input('Enter your username: ')
            password_input = input('Enter your password: ')
            for obj in load_files.accounts:
                if username_input == obj.name and password_input == obj.password:
                    print("login success!")
                    current_user = username_input
                    current_password = password_input
                    log = True
                    loop = False
            if log is False:
                print("login failed, check username and password, you have",
                2 - i, "attempts left", sep =' ')
                i += 1
        else:
            loop is False
    return current_user, password_input
    
